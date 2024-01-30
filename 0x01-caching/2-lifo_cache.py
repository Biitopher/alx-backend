#!/usr/bin/python3
"""LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        """Initiate"""
        super().__init__()
        self.discarded_key = ''

    def put(self, key, item):
        """Put"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.discarded_key))
                self.cache_data.pop(self.discarded_key)
            self.discarded_key = key

    def get(self, key):
        """Get"""
        if key is None  or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
