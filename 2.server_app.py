#!/usr/bin/env python
# using a langchian server

#import config from config.py
from config import set_environment
set_environment()

import os
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

#import packages
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatAnthropic, ChatOpenAI
from langserve import add_routes

import base64
from pdfminer.high_level import extract_pages, extract_text
from langchain.schema.runnable import RunnableLambda
from langserve import CustomUserType, add_routes
from langchain.pydantic_v1 import Field
from langchain.document_loaders.parsers.pdf import PDFMinerParser
from langchain.document_loaders.blob_loaders import Blob


#create an app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
)


model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

add_routes(
    app,
    prompt | model,
    path="/joke",
)

# add a widget for file upload and process
class FileProcessingRequest(CustomUserType):
    """Request including a base64 encoded file."""

    # The extra field is used to specify a widget for the playground UI.
    file: str = Field(..., extra={"widget": {"type": "base64file"}})
    num_chars: int = 100


def _process_file(request: FileProcessingRequest) -> str:
    """Extract the text from the first page of the PDF."""
    content = base64.b64decode(request.file.encode("utf-8"))
    blob = Blob(data=content)
    documents = list(PDFMinerParser().lazy_parse(blob))
    content = documents[0].page_content
    return content[: request.num_chars]

add_routes(
    app,
    RunnableLambda(_process_file).with_types(input_type=FileProcessingRequest),
    config_keys=["configurable"],
    path="/pdf",
)


## run the server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)