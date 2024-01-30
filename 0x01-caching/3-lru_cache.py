#!/usr/bin/env python3
"""LRUCache caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Maintaines an ordered list of keys"""
    def __init__(self):
        """Initializes the LRU cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Indicates when a new item is added"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Updates the order list to reflect the most recent used key"""
        if key is not None:
            value = self.cache_data.get(key, None)
            if value is not None:
                self.order.remove(key)
                self.order.append(key)
            return value
        return None
