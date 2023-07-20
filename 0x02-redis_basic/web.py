#!/usr/bin/env python3
''' task 5: implement an expiring web cache and tracker '''
import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()


def count_requests(method: Callable) -> Callable:
    ''' decorator for counting '''
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        ''' wrapper for decorator '''
        redis_store.incr(f'count:{url}')
        cached_html = redis_store.get(f'cached:{url}')
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_store.setex(f'cached:{url}', 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    ''' obtain the HTML content of a  URL '''
    return requests.get(url).text
