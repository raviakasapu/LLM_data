import os
OPENAI_API_KEY = "add your OpenAI key"
HUGGINGFACEHUB_API_TOKEN = "changed  file"
#export TAVILY_API_KEY= 

def set_environment():
    variable_dict = globals().items()
    for key, value in variable_dict:
        if "API" in key or "ID" in key:
            os.environ[key] = value
