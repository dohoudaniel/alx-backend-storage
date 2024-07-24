#!/usr/bin/env python3
"""
A Python function that lists all documents in a collection
"""


# Import statements
import pymongo


def list_all(mongo_collection):
    """
    Returns a list of all documents in a collection
    """
    if not mongo_collection:
        return []
    return [doc for doc in mongo_collection.find()]
