#!/usr/bin/env python3
"""
Main file
"""
# Code for task 0 and 1
# import redis
#
# Cache = __import__('exercise').Cache
#
# cache = Cache()
#
# data = b"hello"
# key = cache.store(data)
# print(key)
#
# local_redis = redis.Redis()
# print(local_redis.get(key))
#
#
# Code for task 2
Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
