from config import set_environment
set_environment()

import os
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

from langchain.chains import create_extraction_chain
from langchain.chat_models import ChatOpenAI

schema = {
    "properties": {
        "company": {"type": "string"},
        "offering": {"type": "string"},
        "advanttage": {"type": "string"},
        "product_and_services": {"type": "string"},
        "additional_details": {"type": "string"}
    }
}

# Inputs
in1 = """Sweet Delights Bakery introduced lavender-infused vanilla cupcakes with a honey buttercream frosting, using the "Frosting-Spreader-3000". This innovation could inspire our next cupcake creation"""
in2 = """Whisked Away Cupcakes introduced a dessert subscription service, ensuring regular customers receive fresh batches of various sweets. Exploring a similar subscription model using the "SweetSubs" program could boost customer loyalty."""
in3 = """At Velvet Frosting Cupcakes, our team learned about the unveiling of a seasonal pastry menu that changes monthly. Introducing a rotating seasonal menu at our bakery using the "SeasonalJoy" subscription platform and adding a special touch to our cookies with the "FloralStamp" cookie stamper could keep our offerings fresh and exciting for customers."""

inputs = [in1, in2, in3]

#llm = ChatOpenAI(temparature = 0, model="gpt-3.5-turbo")
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
chain = create_extraction_chain(schema=schema, llm=llm)

for input in inputs:
    print(chain.invoke(input)['text'])
    
