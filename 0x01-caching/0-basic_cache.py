#!/usr/bin/env python3
"""0: Basic dictionary caching"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary caching"""

    def put(self, key, item):
        '''assign to the dictionary `self.cache_data` the item'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""

        return self.cache_data.get(key, None)
