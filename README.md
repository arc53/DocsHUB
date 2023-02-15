<h1 align="center">
  DocsHUB 
</h1>

<p align="center">
  <strong>Repository to store and share vector stores / embedding for LLM models</strong>
</p>

<p align="left">
  <strong>DocsHUB</strong> is a open-source solution for storing vectors for LLM models. Like a package manager but for vector stores.
  
Say goodbye to time-consuming scraping and embedding, and let <strong>DocsHUB</strong> speed up your project by providing you with latest embeddings
</p>



## Todo list
- Github workflows to prepare json document with indexes ✅
- Public list to make it usable (index) ✅
- Website with search
- API for search




## [Join Our Parent Project DocsGPT Discord](https://discord.gg/n5BX8dh8rU)


## Project structure
vectors - where all vecor stores are

ingestors - scripts to prepare and ingest data into vector stores


## How to use it:
Just navigate to a folder you need ```vectors/<language>/<library_name>/<version>/<embeddings_model>```
And download:
docs.index, faiss_store.pkl

You can also use this index to find items you need in here (updated on every push)

```https://d3dg1063dc54p9.cloudfront.net/combined.json```

## How to contribute:
Anyone can create a pull request. It should contain 3 files
1. index.faiss
2. index.pkl
3. metadata.json


Ensure the path is correct 
```
  vectors/<language>/<library_name>/<version>/<embeddings_model>
```

if its actual python (language itself) for example use
```
vectors/python/.project/version/
```
And in a corresponding path

Metadata is a json document with this fields:
- name
- language
- version
- description (one or two sectences)
- fullName (Full project name not a slug name)
- date (to know when it was last updated)
- docLink (link to the documentation that was used for it)
- model (embeddings model that was used to generate the vectors

For embeddings model please use ```<providerName_modelName>```
Example:
```
OpenAI:
openai_text-embedding-ada-002

Huggingface:
huggingface_sentence-transformers/all-mpnet-base-v2

Cohere:
cohere_medium
```

Example of metadata.json
```
{
  "name": "pandas",
  "language": "python",
  "version": "1.5.3",
  "description": "Pandas is alibrary providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.",
  "fullName": "Pandas",
  "date": "07/02/2023",
  "docLink": "https://pandas.pydata.org/docs/",
  "model": "openai_text-embedding-ada-002"
}
```

Built with [🦜️🔗 LangChain](https://github.com/hwchase17/langchain)

