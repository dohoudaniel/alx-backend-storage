#!/usr/bin/env python3
"""
Using Redis for basic
operations with Python,
and as a cache also
"""


# Import statements
import redis
import uuid
from typing import Union


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
