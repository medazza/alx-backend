#!/usr/bin/python3
""" 1. FIFO caching module """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Assign to the dictionary"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = next(iter(self.cache_data))
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        if key in self.cache_data:
            return self.cache_data.get(key)
