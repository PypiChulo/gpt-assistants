import os

from dotenv import load_dotenv
load_dotenv()

import openai


def init_openai(api_key=None):
    if api_key is None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise Exception("unknown openai api key")
        
    openai.api_key = api_key
    openai.api_base = "https://api.openai.com/v1"
    openai.api_type = "open_ai"
    openai.api_version = None

    os.environ['OPENAI_API_KEY'] = api_key