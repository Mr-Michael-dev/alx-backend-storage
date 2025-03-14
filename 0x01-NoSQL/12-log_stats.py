#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats():
    """
    prints nginx log status
    """

    # Connect to MongoDB
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Count the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count the number of logs for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count the number of logs with method GET and path /status
    status_check = collection.count_documents({"method": "GET",
                                               "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
