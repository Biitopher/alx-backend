#!/usr/bin/env python3
"""caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class basic cache"""
    def put(self, key, item):
        """Put cache in the dictionary"""
        if key and item:
            self.cache_data[key] = item


    def get(self, key):
        """Get cache to return value"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
