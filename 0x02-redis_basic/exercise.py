#!/usr/bin/env python3
"""
this module contains a class Cache wity method that stores string to redis
"""
import redis
import uuid
from typing import Union


class Cache():
    """
    Stores string to redis

    Methods:
    __init__: instantiation method
    store: takes one argument 'data' and stores it
    """

    def __init__(self):
        """
        stores and instance of the Redis client as a private variable
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, float, bytes]) -> str:
        """
        generate a random key using uuid, store the input data in Redis

        Arguments:
        data: can be a str, bytes, int or float to be stored

        Returns:
        The random key generated
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
