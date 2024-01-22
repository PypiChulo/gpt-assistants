import os

from requests import request
from src.http_utils import a_request


API_KEY = os.environ.get("OPENAI_API_KEY")
HEADERS = {
    "Authorization": "Bearer " + API_KEY,
    "OpenAI-Beta": "assistants=v1"
    }


def format_get_list_args():
        return {
            "url": "https://api.openai.com/v1/assistants",
            "method": "GET",
            "headers": HEADERS
        }
    
def format_create_args(model, name=None, description=None, instructions=None,
                       tools=None, file_ids=None, metadata=None):
    body = {
            "model": model,
            "name": name,
            "description": description,
            "instructions": instructions,
            "tools": tools,
            "file_ids": file_ids,
            "metadata": metadata
        }
    body = {k: v for k, v in body.items() if v is not None}
    return {
        "url": "https://api.openai.com/v1/assistants",
        "method": "POST",
        "json": body,
        "headers": HEADERS
    }
    
def format_update_args(assistant_id, model, name=None, description=None, instructions=None,
                       tools=None, file_ids=None, metadata=None):
    body = {
            "model": model,
            "name": name,
            "description": description,
            "instructions": instructions,
            "tools": tools,
            "file_ids": file_ids,
            "metadata": metadata
        }
    body = {k: v for k, v in body.items() if v is not None}
    return {
        "url": f"https://api.openai.com/v1/assistants/{assistant_id}",
        "method": "POST",
        "json": body,
        "headers": HEADERS
    }
    
def format_attach_file_args(assistant_id, file_id):
    return {
        "url": f"https://api.openai.com/v1/assistants/{assistant_id}/files",
        "method": "POST",
        "json": {"file_id": file_id},
        "headers": HEADERS
    }
    
def format_detach_file_args(assistant_id, file_id):
    return {
        "url": f"https://api.openai.com/v1/assistants/{assistant_id}/files/{file_id}",
        "method": "DELETE",
        "headers": HEADERS
    }
    
def format_get_files_list_args(assistant_id, limit, order, after, before):
    params = {
            "limit": limit,
            "order": order,
            "after": after,
            "before": before
        }
    params = {k: v for k, v in params.items() if v is not None}
    return {
        "url": f"https://api.openai.com/v1/assistants/{assistant_id}/files",
        "method": "GET",
        "params": params,
        "headers": HEADERS
    }

def format_retrieve_file_args(assistant_id, file_id):
    return {
        "url": f"https://api.openai.com/v1/assistants/{assistant_id}/files/{file_id}",
        "method": "GET",
        "headers": HEADERS
    }
    
def format_retrieve_args(assistant_id):
    return {
        "url": f"https://api.openai.com/v1/assistants/{assistant_id}",
        "method": "GET",
        "headers": HEADERS
    }
    
def format_delete_args(assistant_id):
    return {
        "url": f"https://api.openai.com/v1/assistants/{assistant_id}",
        "method": "DELETE",
        "headers": HEADERS
    }
    
    
class AssistantClient():
    
    def get_list(self, *args, **kwargs):
        return request(**format_get_list_args(*args, **kwargs)).json()['data'] 
        
    async def a_get_list(self, *args, **kwargs):
        return (await a_request(**format_get_list_args(*args, **kwargs))).json()['data']
    
    def create(self, *args, **kwargs):
        return request(**format_create_args(*args, **kwargs)).json()
    
    async def a_create(self, *args, **kwargs):
        return (await a_request(**format_create_args(*args, **kwargs))).json()
    
    def update(self, *args, **kwargs):
        return request(**format_update_args(*args, **kwargs)).json()
    
    async def a_update(self, *args, **kwargs):
        return (await a_request(**format_update_args(*args, **kwargs))).json()
    
    def attach_file(self, *args, **kwargs):
        return request(**format_attach_file_args(*args, **kwargs)).json()
    
    async def a_attach_file(self, *args, **kwargs):
        return (await a_request(**format_attach_file_args(*args, **kwargs))).json()
    
    def detach_file(self, *args, **kwargs):
        return request(**format_detach_file_args(*args, **kwargs)).json()
    
    async def a_detach_file(self, *args, **kwargs):
        return (await a_request(**format_detach_file_args(*args, **kwargs))).json()
    
    def get_files_list(self, *args, **kwargs):
        return request(**format_get_files_list_args(*args, **kwargs)).json()['data']
    
    async def a_get_files_list(self, *args, **kwargs):
        return (await a_request(**format_get_files_list_args(*args, **kwargs))).json()['data']
    
    def retrieve_file(self, *args, **kwargs):
        return request(**format_retrieve_file_args(*args, **kwargs)).json()
    
    async def a_retrieve_file(self, *args, **kwargs):
        return (await a_request(**format_retrieve_file_args(*args, **kwargs))).json()
    
    def retrieve(self, *args, **kwargs):
        return request(**format_retrieve_args(*args, **kwargs)).json()
    
    async def a_retrieve(self, *args, **kwargs):
        return (await a_request(**format_retrieve_args(*args, **kwargs))).json()
    
    def delete(self, *args, **kwargs):
        return request(**format_delete_args(*args, **kwargs)).json()
    
    async def a_delete(self, *args, **kwargs):
        return (await a_request(**format_delete_args(*args, **kwargs))).json()