#!/usr/bin/env python3
"""basic caching module"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class"""

    def put(self, key, item):
        """put method"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get method"""
        return self.cache_data.get(key, None)
