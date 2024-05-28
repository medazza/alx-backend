#!/usr/bin/python3
"""2. LIFO Caching module"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """"Class LIFOCache that inherits from BaseCaching"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = list(self.cache_data.keys())[-1]
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key."""
        return self.cache_data.get(key, None)
