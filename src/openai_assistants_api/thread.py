import os

from src.openai_assistants_api.methods_utils import bind_formatter, as_request


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
            "url": "https://api.openai.com/v1/assistants",
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
    
    @bind_formatter(format_create_args)
    @as_request()
    def create(self, **kwargs):
        pass
    
    @bind_formatter(format_create_args)
    @as_request(async_method=True)
    async def a_create(self, **kwargs):
        pass
    
    @bind_formatter(format_retrieve_args)
    @as_request()
    def retrieve(self, **kwargs):
        pass
        
    @bind_formatter(format_retrieve_args)
    @as_request(async_method=True)
    async def a_retrieve(self, **kwargs):
        pass
    
    @bind_formatter(format_update_args)
    @as_request()
    def update(self, **kwargs):
        pass
    
    @bind_formatter(format_update_args)
    @as_request(async_method=True)
    async def a_update(self, **kwargs):
          pass
        
    @bind_formatter(format_delete_args)
    @as_request()
    def delete(self, **kwargs):
        pass
    
    @bind_formatter(format_delete_args)
    @as_request(async_method=True)
    async def a_delete(self, **kwargs):
        pass