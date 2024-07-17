#!/usr/bin/env python3
"""
Update topics of a school document based on the name
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document

    Parameters:
    - mongo_collection: pymongo collection object
    - name (string): the school name to update
    - topics (list of strings): the list of topics approached in the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
