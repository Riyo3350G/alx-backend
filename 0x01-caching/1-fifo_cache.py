#!/usr/bin/env python3
"""fifo caching module"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache Class"""
    def __int__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > super().MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                self.cache_data.pop(first_item)
                print("DISCARD: {}".format(first_item))

    def get(self, key):
        """get method"""
        return self.cache_data.get(key, None)
