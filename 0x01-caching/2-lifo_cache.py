#!/usr/bin/env python3
"""lifo caching module"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class"""
    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > super().MAX_ITEMS:
                last_item = list(self.cache_data.keys())[-1]
                self.cache_data.pop(last_item)
                print("DISCARD: {}".format(last_item))

    def get(self, key):
        """get method"""
        return self.cache_data.get(key, None)
