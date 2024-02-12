#import config from config.py
from config import set_environment
set_environment()

import os
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

#import packages needed
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#create LLM - OpenAI
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

#create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a document writer"),
    ("user","{input}")
])

#set output 
output_parser = StrOutputParser()

#create a chain with prompt --> llm --> output
chain = prompt | llm | output_parser

#invoke the chian with the input
response = chain.invoke({"input": "How can langsmith help with testing"})
print(response)


