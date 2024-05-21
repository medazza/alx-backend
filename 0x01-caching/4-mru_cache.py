#!/usr/bin/python3
"""4: MRU Caching module"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """Class MRUCache that inherits from BaseCaching"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.order.pop()
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieves an item by key."""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key, None)
