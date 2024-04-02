#!/usr/bin/env python3
"""
redis tutorial
"""
import redis
import uuid


class Cache():
    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """
        stores a data in redis
        """
        u_id = str(uuid.uuid4())
        self._redis.set(u_id, data)
        return u_id

    def get(self, key, fn):
        """
        retrieves data from redis server
        with right type
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value
