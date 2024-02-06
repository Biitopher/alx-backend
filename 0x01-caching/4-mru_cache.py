#!/usr/bin/env python3
"""caching system"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class maintains an ordered list"""
    def __init__(self):
        """initializes MRU cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Checks number of items when new item is added"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop()
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Updates order list to reflect most recent used key"""
        if key is not None:
            value = self.cache_data.get(key, None)
            if value is not None:
                self.order.remove(key)
                self.order.append(key)
            return value
        return None
