#!/usr/bin/python3
"""5. LFU Caching module"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Class LFUCache that inherits from BaseCaching"""
    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.freq.values())
                least_freq_keys = [
                    k for k, v in self.freq.items() if v == min_freq
                ]
                lfu_key = min(least_freq_keys, key=self.freq.get)
                self.cache_data.pop(lfu_key)
                self.freq.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.freq[key] = 1
        else:
            self.cache_data[key] = item
            self.freq[key] += 1

    def get(self, key):
        """Retrieves an item by key."""
        if key is None:
            return None
        if key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data.get(key, None)
