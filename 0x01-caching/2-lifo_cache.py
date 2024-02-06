#!/usr/bin/env python3
"""LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Defines class  LIFO Cache that inherits from BaseCaching"""
    def __init__(self):
        """Initialize the LIFO cache"""
        super().__init__()
        self.discarded_key = ''

    def put(self, key, item):
        """Checks if the number of items exceed"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.discarded_key))
                self.cache_data.pop(self.discarded_key)
            self.discarded_key = key

    def get(self, key):
        """Returns vallue associated with key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
