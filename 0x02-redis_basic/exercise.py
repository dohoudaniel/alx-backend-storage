#!/usr/bin/env python3
"""
Using Redis for basic
operations with Python,
and as a cache also
"""


# Import statements
from functools import wraps  # For decorators
import redis
import uuid
from typing import Union, Callable


# Defining the decorators above the Cache class
def count_calls(method: Callable) -> Callable:
    """
    Returns a Callable object
    """
    # Creating a __qualname__ dunder method for a key
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A Wrapper for decorated function
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    A cache class
    """

    def __init__(self):
        """
        Constructor method that stores
        an instance of the Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method that takes a data argument
        and returns a key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self,
            key: str,
            fn: Callable = None) -> Union[str,
                                          bytes,
                                          int,
                                          float]:
        """
        Method that takes a key argument
        and returns the data
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """
        automatically parametrizes Cache.get
        with the correct
        conversion function
        """
        value = self._redis.get(data)
        return value.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """
        automatically parametrizes Cache.get
        with the correct conversion function
        """
        value = self._redis.get(data)
        try:
            new_value = int(value.decode("utf-8"))
        except Exception:
            new_value = 0
        return new_value
