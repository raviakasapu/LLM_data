import os
OPENAI_API_KEY = "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"
HUGGINGFACEHUB_API_TOKEN = "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"
#export TAVILY_API_KEY= 

def set_environment():
    variable_dict = globals().items()
    for key, value in variable_dict:
        if "API" in key or "ID" in key:
            os.environ[key] = value
