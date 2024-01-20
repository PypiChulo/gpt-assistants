from requests import request

import openai

from http_utils import a_request


class Assistant():       
    
    def format_get_list_args(self):
        return {
            "url": "https://api.openai.com/v1/assistants",
            "method": "GET"
        }
    
    def format_create_args(self, model, name, description,
                           instructions, tools, file_ids, metadata):
        return {
            "url": "https://api.openai.com/v1/assistants",
            "method": "POST",
            "json": {
                "model": model,
                "name": name,
                "description": description,
                "instructions": instructions,
                "tools": tools,
                "file_ids": file_ids,
                "metadata": metadata
            }
        }
    
    def format_retrieve_args(self, assistant_id):
        return {
            "url": f"https://api.openai.com/v1/assistants/{assistant_id}",
            "method": "GET"
        }
    
    def format_delete_args(self, assistant_id):
        return {
            "url": f"https://api.openai.com/v1/assistants/{assistant_id}",
            "method": "DELETE"
        }
    
    def get_list(self):
        request_args = self.format_get_list_params()
        response = request(**request_args).json()
        return response
        
    async def a_get_list(self):
        request_args = self.format_get_list_params()
        response = a_request(**request_args).json()
        return response
    
    def create(self):
        request_args = self.format_create_params()
        response = request(**request_args).json()
        return response
    
    async def a_create(self):
        request_args = self.format_create_params()
        response = a_request(**request_args).json()
        return response
    
    def retrieve(self):
        request_args = self.format_retrieve_params() 
        response = request(**request_args).json()
        return response
    
    async def a_retrieve(self):
        request_args = self.format_retrieve_params() 
        response = a_request(**request_args).json()
        return response
    
    def delete(self):
        request_args = self.format_delete_params()
        response = request(**request_args).json()
        return response
    
    async def a_delete(self):
        request_args = self.format_delete_params()
        response = a_request(**request_args).json()
        return response