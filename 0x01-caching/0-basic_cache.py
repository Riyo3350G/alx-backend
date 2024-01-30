#!/usr/bin/env python3
"""basic caching module"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class"""

    def put(self, key, item):
        """put method"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
