#!/usr/bin/env python3
"""
Python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    returns the new document id
    """
    newDoc = mongo_collection.insert_one(kwargs)

    return (newDoc.inserted_id)
