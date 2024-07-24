#!/usr/bin/env python3
"""
A Python function that returns the list of school
having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic searched
"""


# Import statements
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
