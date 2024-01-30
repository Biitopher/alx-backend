#!/usr/bin/python3
"""FIFO Cache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """Initiate"""
        super().__init__()

    def put(self, key, item):
        """Put"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key, _ = next(iter(self.cache_data.items()))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """Get"""
        if key is not None:
            return self.cache_data.get(key, None)
        return None
