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
- Github workflows to prepare json document with indexes
- Website with search and index
- Plugin with DocsGPT
- Plugins for other projects
- API for search




## [Join Our parent projecs DocsGPT Discord](https://discord.gg/n5BX8dh8rU)


## Project structure
vectors - where all vecor stores are

ingestors - scripts to prepare and ingest data into vector stores


## How to use it:
Just navigate to a folder you need ```vectors/<language>/<library_name>/<version>/```
And download:
docs.index, faiss_store.pkl

## How to contribute:
Anyone can create a pull request. It should contain 3 files
1. docs.index
2. faiss_store.pkl
3. metadata.json


Ensure the path is correct 
```
  vectors/<language>/<library_name>/<version>/
```

if its python for example use
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



Built with [🦜️🔗 LangChain](https://github.com/hwchase17/langchain)

