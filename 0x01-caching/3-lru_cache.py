#!/usr/bin/env python3
"""lru caching module"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache Class"""
    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > super().MAX_ITEMS:
                recent_item = list(self.cache_data.keys())[0]
                self.cache_data.pop(recent_item)
                print("DISCARD: {}".format(recent_item))

    def get(self, key):
        """get method"""
        return self.cache_data.get(key, None)
