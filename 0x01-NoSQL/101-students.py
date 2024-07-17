#!/usr/bin/env python3
"""
Function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns students sorted by average score

    Parameters:
    mongo_collection: pymongo collection object
    """
    pipeline = [
        {"$unwind": "$topics"},  # Deconstruct the topics array
        {"$group": {
            "_id": "$_id",
            # Compute average score for topics.score
            "averageScore": {"$avg": "$topics.score"}
        }},
        # Sort by averageScore in descending order
        {"$sort": {"averageScore": -1}}
    ]

    students = list(mongo_collection.aggregate(pipeline))
    return students
