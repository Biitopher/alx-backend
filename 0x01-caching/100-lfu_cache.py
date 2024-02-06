#!/usr/bin/env python3
"""caching system"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class LFUCache maintains frequency dictionary"""
    def __init__(self):
        """Initializes LFU cache"""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Checks if new item is added in number of items"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                least_frequent_keys = ([k for k, v in self.frequency.items()
                                       if v == min_frequency])

                if len(least_frequent_keys) == 1:
                    discarded_key = least_frequent_keys[0]
                else:
                    discarded_key = self.lru_discard(least_frequent_keys)

                del self.cache_data[discarded_key]
                del self.frequency[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """Updates frequency of key"""
        if key is not None:
            value = self.cache_data.get(key, None)
            if value is not None:
                self.frequency[key] += 1
            return value
        return None

    def lru_discard(self, keys):
        """Discards least recently used item in the list"""
        return min(keys, key=lambda k: self.frequency[k])
