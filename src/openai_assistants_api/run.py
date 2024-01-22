import os

from requests import request
from src.http_utils import a_request


API_KEY = os.environ.get("OPENAI_API_KEY")
HEADERS = {
    "Authorization": "Bearer " + API_KEY,
    "OpenAI-Beta": "assistants=v1"
    }


def format_create_args(thread_id, assistant_id, model=None, instructions=None,
                       additional_instructions=None, tool=None, metadata=None):
    body = {
            "assistant_id": assistant_id,
            "model": model,
            "instructions": instructions,
            "additional_instructions": additional_instructions,
            "tool": tool,
            "metadata": metadata
        }
    body = {k: v for k, v in body.items() if v is not None}
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/runs",
        "method": "POST",
        "json": body,
        "headers": HEADERS
    }
    

def format_create_thread_and_run(assistant_id, thread=None, model=None, instructions=None,
                          additional_instructions=None, tool=None, metadata=None):
    body = {
            "assistant_id": assistant_id,
            "thread": thread,
            "model": model,
            "instructions": instructions,
            "additional_instructions": additional_instructions,
            "tool": tool,
            "metadata": metadata
        }
    body = {k: v for k, v in body.items() if v is not None}
    return {
        "url": f"https://api.openai.com/v1/threads/runs",
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
        "url": f"https://api.openai.com/v1/threads/{thread_id}/runs",
        "method": "GET",
        "params": params,
        "headers": HEADERS
    }
    
    
def format_get_steps_list_args(thread_id, run_id, limit=None, order=None, after=None, before=None):
    params = {
        "limit": limit,
        "order": order,
        "after": after,
        "before": before
    }
    params = {k: v for k, v in params.items() if v is not None}
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/steps",
        "method": "GET",
        "params": params,
        "headers": HEADERS
    }
    
    
def format_retrieve_args(thread_id, run_id):
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}",
        "method": "GET",
        "headers": HEADERS
    }
    
    
def format_retrieve_step_args(thread_id, run_id, step_id):
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/steps/{step_id}",
        "method": "GET",
        "headers": HEADERS
    }
    
    
def format_update_args(thread_id, run_id, metadata=None):
    body = {"metadata": metadata} if metadata else {}
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}",
        "method": "POST",
        "json": body,
        "headers": HEADERS
    }
    
    
def format_submit_tool_outputs(thread_id, run_id, step_id, tool_outputs):
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/steps/{step_id}/submit_tool_outputs",
        "method": "POST",
        "json": {"tool_outputs": tool_outputs},
        "headers": HEADERS
    }
    
    
def format_cancel_args(thread_id, run_id):
    return {
        "url": f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/cancel",
        "method": "POST",
        "headers": HEADERS
    }


class RunClient():
    
    def create(self, *args, **kwargs):
        return request(**format_create_args(*args, **kwargs)).json()
    
    async def a_create(self, *args, **kwargs):
        return (await a_request(**format_create_args(*args, **kwargs))).json()
    
    def create_thread_and_run(self, *args, **kwargs):
        return request(**format_create_thread_and_run(*args, **kwargs)).json()
    
    async def a_create_thread_and_run(self, *args, **kwargs):
        return (await a_request(**format_create_thread_and_run(*args, **kwargs))).json()
    
    def get_list(self, *args, **kwargs):
        return request(**format_get_list_args(*args, **kwargs)).json()['data']
    
    async def a_get_list(self, *args, **kwargs):
        return (await a_request(**format_get_list_args(*args, **kwargs))).json()['data']
    
    def get_steps_list(self, *args, **kwargs):
        return request(**format_get_steps_list_args(*args, **kwargs)).json()['data']
    
    async def a_get_steps_list(self, *args, **kwargs):
        return (await a_request(**format_get_steps_list_args(*args, **kwargs))).json()['data']
    
    def retrieve(self, *args, **kwargs):
        return request(**format_retrieve_args(*args, **kwargs)).json()
    
    async def a_retrieve(self, *args, **kwargs):
        return (await a_request(**format_retrieve_args(*args, **kwargs))).json()
    
    def retrieve_step(self, *args, **kwargs):
        return request(**format_retrieve_step_args(*args, **kwargs)).json()
    
    async def a_retrieve_step(self, *args, **kwargs):
        return (await a_request(**format_retrieve_step_args(*args, **kwargs))).json()
    
    def update(self, *args, **kwargs):
        return request(**format_update_args(*args, **kwargs)).json()
    
    async def a_update(self, *args, **kwargs):
        return (await a_request(**format_update_args(*args, **kwargs))).json()
    
    def submit_tool_outputs(self, *args, **kwargs):
        return request(**format_submit_tool_outputs(*args, **kwargs)).json()
    
    async def a_submit_tool_outputs(self, *args, **kwargs):
        return (await a_request(**format_submit_tool_outputs(*args, **kwargs))).json()
    
    def cancel(self, *args, **kwargs):
        return request(**format_cancel_args(*args, **kwargs)).json()
    
    async def a_cancel(self, *args, **kwargs):
        return (await a_request(**format_cancel_args(*args, **kwargs))).json()