#!/usr/bin/env python3
"""
A Python function that inserts a new document
in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id
"""


# Import statement
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection
    using variable arguments in Python
    """
    return mongo_collection.insert(kwargs)
