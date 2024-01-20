import functools
from requests import request
from src.http_utils import a_request


def bind_formatter(formatter):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            formatted_args = formatter(*args, **kwargs)
            return func(self, **formatted_args)
        return wrapper
    return decorator


def as_request(async_method=False, is_list=False):
    def decorator(func):
        @functools.wraps(func)
        def sync_wrapper(_, *args, **kwargs):
            response = request(*args, **kwargs)
            return response.json()['data'] if is_list else response.json()

        @functools.wraps(func)
        async def async_wrapper(_, *args, **kwargs):
            response = await a_request(*args, **kwargs)
            return response.json()['data'] if is_list else response.json()

        if async_method:
            return async_wrapper
        else:
            return sync_wrapper

    return decorator