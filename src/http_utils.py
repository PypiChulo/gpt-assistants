import httpx

from typing import Optional, Dict, Any


async def a_request(method: str, url: str,
                    params: Optional[Dict[str, Any]] = None,
                    data: Optional[Dict[str, Any]] = None,
                    json: Optional[Dict[str, Any]] = None,
                    headers: Optional[Dict[str, str]] = None) -> httpx.Response:
    """
    Makes an asynchronous HTTP request using the given parameters.

    :param method: The HTTP method to use (e.g., 'GET', 'POST', 'PATCH').
    :param url: The URL to make the request to.
    :param params: Optional dict of query parameters to append to the URL.
    :param data: Optional dict of form data to send in the body of the request.
    :param json: Optional dict to send as JSON in the body of the request.
    :param headers: Optional dict of headers to include in the request.
    :return: The httpx Response object.
    """
    async with httpx.AsyncClient() as client:
        response = await client.request(method=method,
                                        url=url,
                                        params=params,
                                        data=data,
                                        json=json,
                                        headers=headers)
        return response