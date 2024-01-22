import os

from requests import request
from src.http_utils import a_request


API_KEY = os.environ.get("OPENAI_API_KEY")
HEADERS = {
    "Authorization": "Bearer " + API_KEY,
    "OpenAI-Beta": "assistants=v1"
    }


def format_create_args(messages=None, metadata=None):
        body = {
            "messages": messages,
            "metadata": metadata
        }
        body = {k: v for k, v in body.items() if v is not None}
        return {
            "url": "https://api.openai.com/v1/threads",
            "method": "POST",
            "json": body,
            "headers": HEADERS
        }
        
        
def format_retrieve_args(thread_id):
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}",
        "method": "GET",
        "headers": HEADERS
    }
    
    
def format_update_args(thread_id, metadata=None):
    body = {"metadata": metadata} if metadata else {}
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}",
        "method": "POST",
        "json": body,
        "headers": HEADERS
    }
    
    
def format_delete_args(thread_id):
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}",
        "method": "DELETE",
        "headers": HEADERS
    }
    

class ThreadClient():
    
    def create(self, *args, **kwargs):
        return request(**format_create_args(*args, **kwargs)).json()
    
    async def a_create(self, *args, **kwargs):
        return (await a_request(**format_create_args(*args, **kwargs))).json()
    
    def retrieve(self, *args, **kwargs):
        return request(**format_retrieve_args(*args, **kwargs)).json()
    
    async def a_retrieve(self, *args, **kwargs):
        return (await a_request(**format_retrieve_args(*args, **kwargs))).json()
    
    def update(self, *args, **kwargs):
        return request(**format_update_args(*args, **kwargs)).json()
    
    async def a_update(self, *args, **kwargs):
        return (await a_request(**format_update_args(*args, **kwargs))).json()
    
    def delete(self, *args, **kwargs):
        return request(**format_delete_args(*args, **kwargs)).json()
    
    async def a_delete(self, *args, **kwargs):
        return (await a_request(**format_delete_args(*args, **kwargs))).json()
    
    