# DocSum: Document and Image Summarizer

A simple Python CLI tool that summarizes either text-based documents (like HTML files) or images using Groq's LLM and vision models.

## Features

- Summarizes text documents using `llama3-8b-8192`
- Summarizes images (local files or URLs) using `llama-4-scout-17b-16e-instruct`
- Automatically detects whether input is text or image

## Requirements

- Python 3.8+
- `groq`, `beautifulsoup4`, `lxml`, `python-dotenv`

## Examples

$ python3 docsum.py docs/news-mx.html
The US Supreme Court has lifted the temporary suspension of a 1798 law allowing President Trump to deport immigrants accused of being affiliated with a criminal organization in Venezuela, known as the "Tren de Aragua", without a formal trial. The decision, made by a 5-4 vote, allows the deportations to continue, although the immigrant must be given the opportunity to appeal their removal. The court's decision is seen as a victory for Trump, who has been seeking to use the law to crack down on unauthorized immigration.

$ python3 docsum.py docs/constitution-mx.txt
The Mexican Constitution of 1917, with subsequent reforms, recognizes and guarantees the rights of indigenous peoples, including self-determination, autonomy, and cultural preservation. The constitution outlines the structure and powers of the government, including the legislative, executive, and judicial branches, as well as the rights and responsibilities of citizens. Additionally, the constitution addresses various social and economic issues, such as workers' rights, labor protections, and the organization of municipalities and metropolitan areas.

$ python3 docsum.py docs/research_paper.pdf
DOCSPLIT is an unsupervised pretraining method designed specifically for large documents that uses a contrastive loss to force models to consider the global context of a document, resulting in high-quality document embeddings. The method outperforms other pretraining methods on document classification, few-shot learning, and document retrieval tasks, achieving state-of-the-art performance with the LongFormer-based DOCSPLITlong model.

$ python3 docsum.py https://elpais.com/us/
The text is a news article from the El País newspaper, covering a wide range of topics including politics, economy, culture, and sports. The article mentions the ongoing trade war between China and the United States, with China raising its tariffs to 125% and President Trump facing a marathon of trade negotiations. The article also touches on other news stories, including the death of five Spanish tourists in a helicopter crash in New York, the ongoing migrant crisis in the US, and the impact of the COVID-19 pandemic on the global economy.

$ python3 docsum.py https://www.cmc.edu/sites/default/files/about/images/20170213-cube.jpg
The image depicts a modern building with a glass-enclosed section, featuring a pool of water in front and a dark blue sky in the background.

* The glass-enclosed section:
        + Has a black frame
        + Is square-shaped
        + Has a flat roof
        + Is well-lit from inside
        + Contains several orange and yellow chairs
        + Appears to be a lounge or meeting area
* The pool of water:
        + Is rectangular
        + Reflects the lights from the building
        + Has a small square section on the left side
* The surrounding buildings:
        + Are multi-story
        + Have balconies with glass railings
        + Are well-lit from inside
        + Appear to be office or residential spaces
* The sky:
        + Is dark blue
        + Has some clouds

The image presents a serene and modern architectural scene, with a focus on clean lines, minimalism, and functionality. The use of glass, steel, and water creates a sense of calmness and sophistication.