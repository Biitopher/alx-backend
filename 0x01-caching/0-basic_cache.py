#!/usr/bin/python3
"""caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """Put cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get cache"""
        if key is not None:
            return self.cache_data.get(key, None)
        return None
