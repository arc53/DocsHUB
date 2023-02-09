from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import ReadTheDocsLoader
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle
import dotenv
import tiktoken
import sys
from argparse import ArgumentParser
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')



# wget -r -A.html -P inputs https://gpt-index.readthedocs.io/en/latest/index.html

def num_tokens_from_string(string: str, encoding_name: str) -> int:
# Function to convert string to tokens and estimate user cost.
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    total_price = ((num_tokens/1000) * 0.0004)
    return num_tokens, total_price

def call_openai_api():
# Function to create a vector store from the documents and save it to disk.
    store = FAISS.from_documents(docs, OpenAIEmbeddings())
    faiss.write_index(store.index, "docs.index")
    store.index = None

    with open("faiss_store.pkl", "wb") as f:
        pickle.dump(store, f)


def get_user_permission():
# Function to ask user permission to call the OpenAI api and spend their OpenAI funds.
    # Here we convert the docs list to a string and calculate the number of OpenAI tokens the string represents.
    #docs_content = (" ".join(docs))
    docs_content = ""
    for doc in docs:
        docs_content += doc.page_content


    tokens, total_price = num_tokens_from_string(string=docs_content, encoding_name="cl100k_base")
    # Here we print the number of tokens and the approx user cost with some visually appealing formatting.
    print(f"Number of Tokens = {format(tokens, ',d')}")
    print(f"Approx Cost = ${format(total_price, ',.2f')}")
    #Here we check for user permission before calling the API.
    user_input = input("Price Okay? (Y/N) \n").lower()
    if user_input == "y":
        call_openai_api()
    elif user_input == "":
        call_openai_api()
    else:
        print("The API was not called. No money was spent.")

#Load .env file
dotenv.load_dotenv()

ap = ArgumentParser("Script for training DocsGPT on .rst documentation files.")
ap.add_argument("-i", "--inputs",
                type=str,
                default="inputs",
                help="Directory containing documentation files")
args = ap.parse_args()

# 1st option
# loader = ReadTheDocsLoader("inputs/langchain.readthedocs.io")
# raw_documents = loader.load()

from langchain.document_loaders import UnstructuredHTMLLoader
ps = list(Path("inputs/gpt-index.readthedocs.io").glob("**/*.html"))
len(ps)
raw_documents = []
for p in ps:
    print(p)
    loader = UnstructuredHTMLLoader(p)
    raw_document = loader.load()
    for i in raw_document:
        raw_documents.append(i)


# merge all raw documents into one


print(len(raw_documents))
print(type(raw_documents))
print(type[raw_documents[0]])
print(raw_documents[0])

# Here we split the documents, as needed, into smaller chunks.
# We do this due to the context limits of the LLMs.
text_splitter = RecursiveCharacterTextSplitter()
docs = text_splitter.split_documents(raw_documents)


# Here we check for command line arguments for bot calls.
# If no argument exists or the permission_bypass_flag argument is not '-y',
# user permission is requested to call the API.
if len(sys.argv) > 1:
    permission_bypass_flag = sys.argv[1]
    if permission_bypass_flag == '-y':
        call_openai_api()
    else:
        get_user_permission()
else:
    get_user_permission()
