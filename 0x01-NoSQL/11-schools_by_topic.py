#!/usr/bin/env python3
"""
function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    list all students having a specific topic

    Parameters:
    - mongo_collection: pymongo collection object
    - topic (string): the topic searched for

    Returns:
    list of documents
    """
    return list(mongo_collection.find(
        {"topics": topic}
    ))
