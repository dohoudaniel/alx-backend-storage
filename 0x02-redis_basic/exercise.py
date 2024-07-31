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
from typing import Union, Callable, Optional


# Defining the decorators above the Cache class
def count_calls(method: Callable) -> Callable:
    """
    Returns a Callable object
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A Wrapper for decorated function
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Store history of inputs and
    outputs for a particular function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A wrapper for the decorated
        function call_history
        """
        input = str(args)  # Normalizing
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper


def replay(fn: Callable):
    """
    Display the history of calls of a particular function
    """
    r = redis.Redis()
    function_name = fn.__qualname__
    value = r.get(function_name)
    try:
        value = int(value.decode("utf-8"))
    except Exception:
        value = 0

    # print(f"{function_name} was called {value} times")
    print("{} was called {} times:".format(function_name, value))
    # inputs = r.lrange(f"{function_name}:inputs", 0, -1)
    inputs = r.lrange("{}:inputs".format(function_name), 0, -1)

    # outputs = r.lrange(f"{function_name}:outputs", 0, -1)
    outputs = r.lrange("{}:outputs".format(function_name), 0, -1)

    for input, output in zip(inputs, outputs):
        try:
            input = input.decode("utf-8")
        except Exception:
            input = ""

        try:
            output = output.decode("utf-8")
        except Exception:
            output = ""

        # print(f"{function_name}(*{input}) -> {output}")
        print("{}(*{}) -> {}".format(function_name, input, output))


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

    @count_calls
    @call_history
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
            fn: Optional[Callable] = None) -> Union[str,
                                                    bytes,
                                                    int,
                                                    float]:
        """
        Method that takes a key argument
        and returns the data in the desired
        format
        """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: str) -> str:
        """
        automatically parametrizes Cache.get
        with the correct
        conversion function
        """
        value = self._redis.get(data)
        return value.decode('utf-8')

    def get_int(self, data: str) -> int:
        """
        automatically parametrizes Cache.get
        with the correct conversion function
        """
        value = self._redis.get(data)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
