import os

from src.openai_assistants_api.methods_utils import bind_formatter, as_request


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
        "url": f"https://api.openai.com/v1/threads/{thread_id}/assistants",
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
    
    @bind_formatter(format_create_args)
    @as_request()
    def create(self, **kwargs):
        pass
    
    @bind_formatter(format_create_args)
    @as_request(async_method=True)
    async def a_create(self, **kwargs):
        pass
    
    @bind_formatter(format_create_thread_and_run)
    @as_request()
    def create_thread_and_run(self, **kwargs):
        pass
    
    @bind_formatter(format_create_thread_and_run)
    @as_request(async_method=True)
    async def a_create_thread_and_run(self, **kwargs):
        pass
    
    @bind_formatter(format_get_list_args)
    @as_request()
    def get_list(self, **kwargs):
        pass
    
    @bind_formatter(format_get_list_args)
    @as_request(async_method=True)
    async def a_get_list(self, **kwargs):
        pass
    
    @bind_formatter(format_get_steps_list_args)
    @as_request()
    def get_steps_list(self, **kwargs):
        pass
    
    @bind_formatter(format_get_steps_list_args)
    @as_request(async_method=True)
    async def a_get_steps_list(self, **kwargs):
        pass
    
    @bind_formatter(format_retrieve_args)
    @as_request()
    def retrieve(self, **kwargs):
        pass
    
    @bind_formatter(format_retrieve_args)
    @as_request(async_method=True)
    async def a_retrieve(self, **kwargs):
        pass
    
    @bind_formatter(format_retrieve_step_args)
    @as_request()
    def retrieve_step(self, **kwargs):
        pass
    
    @bind_formatter(format_retrieve_step_args)
    @as_request(async_method=True)
    async def a_retrieve_step(self, **kwargs):
        pass
    
    @bind_formatter(format_update_args)
    @as_request()
    def update(self, **kwargs):
        pass
    
    @bind_formatter(format_update_args)
    @as_request(async_method=True)
    async def a_update(self, **kwargs):
          pass
      
    @bind_formatter(format_submit_tool_outputs)
    @as_request()
    def submit_tool_outputs(self, **kwargs):
        pass
    
    @bind_formatter(format_submit_tool_outputs)
    @as_request(async_method=True)
    async def a_submit_tool_outputs(self, **kwargs):
        pass
        
    @bind_formatter(format_cancel_args)
    @as_request()
    def cancel(self, **kwargs):
        pass
    
    @bind_formatter(format_cancel_args)
    @as_request(async_method=True)
    async def a_cancel(self, **kwargs):
        pass
    