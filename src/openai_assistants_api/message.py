import os

from src.openai_assistants_api.methods_utils import bind_formatter, as_request


API_KEY = os.environ.get("OPENAI_API_KEY")
HEADERS = {
    "Authorization": "Bearer " + API_KEY,
    "OpenAI-Beta": "assistants=v1"
    }


def format_create_args(thread_id, role, content, file_ids=None, metadata=None):
    body = {
            "role": role,
            "content": content,
            "file_ids": file_ids,
            "metadata": metadata
        }
    body = {k: v for k, v in body.items() if v is not None}
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/messages",
        "method": "POST",
        "json": body,
        "headers": HEADERS
    }
    
    
def format_get_list_args(thread_id, limit=None, order=None, after=None, before=None):
    params = {
        "limit": limit,
        "order": order,
        "after": after,
        "before": before
    }
    params = {k: v for k, v in params.items() if v is not None}
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/messages",
        "method": "GET",
        "params": params,
        "headers": HEADERS
    }
    
    
def format_get_files_list_args(thread_id, message_id, limit=None, order=None, after=None, before=None):
    params = {
        "limit": limit,
        "order": order,
        "after": after,
        "before": before
    }
    params = {k: v for k, v in params.items() if v is not None}
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}/files",
        "method": "GET",
        "params": params,
        "headers": HEADERS
    }
    
    
def format_retrieve_args(thread_id, message_id):
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}",
        "method": "GET",
        "headers": HEADERS
    }
    
    
def retrieve_file_args(thread_id, message_id, file_id):
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}/files/{file_id}",
        "method": "GET",
        "headers": HEADERS
    }
    
    
def format_update_args(thread_id, message_id, metadata=None):
    body = {"metadata": metadata} if metadata else {}
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}",
        "method": "POST",
        "json": body,
        "headers": HEADERS
    }
    
    
class MessageClient():
        
        @bind_formatter(format_create_args)
        @as_request()
        def create(self, **kwargs):
            pass
        
        @bind_formatter(format_create_args)
        @as_request(async_method=True)
        async def a_create(self, **kwargs):
            pass
        
        @bind_formatter(format_get_list_args)
        @as_request()
        def get_list(self, **kwargs):
            pass
        
        @bind_formatter(format_get_list_args)
        @as_request(async_method=True)
        async def a_get_list(self, **kwargs):
            pass
        
        @bind_formatter(format_get_files_list_args)
        @as_request()
        def get_files_list(self, **kwargs):
            pass
        
        @bind_formatter(format_get_files_list_args)
        @as_request(async_method=True)
        async def a_get_files_list(self, **kwargs):
            pass
        
        @bind_formatter(format_retrieve_args)
        @as_request()
        def retrieve(self, **kwargs):
            pass
        
        @bind_formatter(format_retrieve_args)
        @as_request(async_method=True)
        async def a_retrieve(self, **kwargs):
            pass
        
        @bind_formatter(retrieve_file_args)
        @as_request()
        def retrieve_file(self, **kwargs):
            pass
        
        @bind_formatter(retrieve_file_args)
        @as_request(async_method=True)
        async def a_retrieve_file(self, **kwargs):
            pass
        
        @bind_formatter(format_update_args)
        @as_request()
        def update(self, **kwargs):
            pass
        
        @bind_formatter(format_update_args)
        @as_request(async_method=True)
        async def a_update(self, **kwargs):
            pass