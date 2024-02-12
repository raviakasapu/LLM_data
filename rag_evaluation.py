from config import set_environment
set_environment()

import os
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

#import web document
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    "https://blog.langchain.dev/langchain-v0-1-0/"
)

documents = loader.load()

#text splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 700,
    chunk_overlap = 50
)

documents = text_splitter.split_documents(documents)

#create embeddings
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

# create vectorstore
from langchain_community.vectorstores import FAISS

vector_store = FAISS.from_documents(documents, embeddings)
retriever = vector_store.as_retriever()
