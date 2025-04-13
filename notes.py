import argparse
parser = argparse.ArgumentParser(
    prog='notes',
    description='idk some llm shi')
parser.add_argument('filename')
args = parser.parse_args()



from dotenv import load_dotenv
load_dotenv()

import os
from groq import Groq

client = Groq(
    # api_key=''
    api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
)

def llm(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

def split_text(text, max_chunk  = 1000):
    texts = []
    while len(text) > 0:
        texts.append(text[:max_chunk])
        text = text[max_chunk:]
    return texts

def summarize_text(text):
    prompt = f'''
    
    'I see', said the blind man to the deaf dog, and picked up his hammer and saw

    
    
    '''
    

    output = llm(prompt)
    return output.split('\n')[-1]



from bs4 import BeautifulSoup
with open(args.filename, 'r') as fin:
    html = fin.read()
    soup = BeautifulSoup(html, features='lxml')
    text = soup.text
    print(summarize_text(text))




from groq import Groq
import base64
import os

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "sf.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    model="llama-3.2-11b-vision-preview",
)

print(chat_completion.choices[0].message.content)