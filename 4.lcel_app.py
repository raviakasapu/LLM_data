from config import set_environment
set_environment()

import os
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

promptt = ChatPromptTemplate.from_template("tell me a joke about {tpoic}")
model = ChatOpenAI(model="gpt-3.5-turbo")
StrOutputParser = StrOutputParser

chain = promptt | model | StrOutputParser()

response = chain.invoke({"tpoic": "ice cream"})
print(response)