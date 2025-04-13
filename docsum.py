import base64
import textract
import requests

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def llm(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                # content = prompt
                # Any time I'm using an LLM,
                # I always provide an instruction about how long
                # the output should be
                "content": text,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

def llm_image(image_url):
    try:
        vision_completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Summarize whats in this image."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            }
                        }
                    ]
                }
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        print(vision_completion.choices[0].message.content)
        return vision_completion.choices[0].message.content

    except groq.BadRequestError:
        base64_image = encode_image(image_url)
        # print(base64_image)
        llm_image(f"data:image/jpeg;base64,{base64_image}")
    
        return 
    

def split_text(text, max_chunk_size=1000):

    accumulator = []
    while len(text) > 0:
        accumulator.append(text[:max_chunk_size])
        text = text[max_chunk_size:]
    return accumulator

def summarize_text(text):

    prompt = f'''
    Summarize the following text in 1-3 sentences.

    {text}
    '''
    try:
        output = llm(prompt)
        return output.split('\n')[-1]
    except groq.APIStatusError:
        chunks = split_text(text, 10000)
        print('len(chunks)=', len(chunks))
        accumulator = []
        for i, chunk in enumerate(chunks):
            print('i=', i)
            # recursion is when you call a function inside itself
            summary = summarize_text(chunk)
            accumulator.append(summary)
        summarized_text = ' '.join(accumulator)
        summarized_text = summarize_text(summarized_text)
        # print('summarized_text=', summarized_text)
        return summarized_text
    
def extract_text_from_pdf(pdf_path):

    text = textract.process(pdf_path, encoding='utf-8')
    return text.decode('utf-8')



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        prog='docsum',
        description='summarize the input document',
        )
    parser.add_argument('filename')

    args = parser.parse_args()

    from dotenv import load_dotenv
    load_dotenv()

    import os
    from groq import Groq
    import groq

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
    )

    from bs4 import BeautifulSoup

    # if args.image:
    #     llm_image(args.image)


    try: 
        with open(args.filename, 'r') as fin:
            html = fin.read()
            soup = BeautifulSoup(html, features="lxml")

            # Remove all <style> and <script> elements
            for tag in soup(['style', 'script']):
                tag.decompose()

            # Get clean text
            text = soup.get_text(separator=' ', strip=True)
            # print(text)
            print(summarize_text(text))
    except (FileNotFoundError, UnicodeDecodeError):
        try:
            llm_image(args.filename)
        except:
            try:
                response = requests.get(args.filename)
                html = response.text
                soup = BeautifulSoup(html, features="lxml")

                    # Remove all <style> and <script> elements
                for tag in soup(['style', 'script']):
                    tag.decompose()

                # Get clean text
                text = soup.get_text(separator=' ', strip=True)
                # print(text)
                print(summarize_text(text))
            except requests.exceptions.MissingSchema:
                try:
                    print(summarize_text(extract_text_from_pdf(args.filename)))
            
                except (textract.exceptions.ShellError, textract.exceptions.MissingFileError):
                    try:
                        llm_image(args.filename)
                    except:
                        print("Invalid document")
    # except (UnicodeDecodeError):
    # #     