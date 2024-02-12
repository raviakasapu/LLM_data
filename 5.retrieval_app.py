from config import set_environment
set_environment()

import os
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")

docs = loader.load()
embeddings = OpenAIEmbeddings()

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)

vector = FAISS.from_documents(documents, embeddings)

prompt = ChatPromptTemplate.from_template(
    """answer the following based only on the provided context
    <context>
    {context}
    </context>

    Question: {input}
    """
)

document_chain = create_stuff_documents_chain(llm, prompt)
retriever = vector.as_retriever()
retriever_chain = create_retrieval_chain(retriever, document_chain)

response = retriever_chain.invoke({"input": "how can langsmith help with testing?"})
print(response["answer"])