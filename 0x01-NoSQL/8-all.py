#!/usr/bin/env python3
"""
Write a Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    returns a cursor object containing list of documents
    """
    documents = mongo_collection.find()

    return list(documents)
