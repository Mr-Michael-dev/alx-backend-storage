#!/usr/bin/env python3
"""
This module contains a class Cache with methods that store and
retrieve data from Redis.
"""

import redis
import uuid
from typing import Any, Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called.

    Arguments:
    method: The method to be decorated.

    Returns:
    A wrapper function that increments the count
    each time the method is called
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count and
        calls the original method.
        """
        key = f"{method.__qualname__}:calls"
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    Stores and retrieves data from Redis.

    Methods:
    __init__: Instantiation method.
    store: Takes one argument 'data' and stores it.
    get: Retrieves data by key and applies an optional conversion function.
    get_str: Retrieves data as a string.
    get_int: Retrieves data as an integer.
    """

    def __init__(self):
        """
        Initializes an instance of the Redis client as a private variable.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key using uuid and stores the input data in Redis.

        Arguments:
        data: Can be a str, bytes, int, or float to be stored.

        Returns:
        The random key generated.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """
        Retrieves data by key and applies an optional conversion function.

        Arguments:
        key: The key to retrieve data from.
        fn: A callable function to convert the data to the desired format.

        Returns:
        The data retrieved and converted by the function if provided,
        otherwise the raw data.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves data as a string.

        Arguments:
        key: The key to retrieve data from.

        Returns:
        The data retrieved as a string.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves data as an integer.

        Arguments:
        key: The key to retrieve data from.

        Returns:
        The data retrieved as an integer.
        """
        return self.get(key, lambda d: int(d))
