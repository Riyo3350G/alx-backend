#!/usr/bin/env python3
"""mru caching module"""
from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """LRUCache Class"""
    def __init__(self):
        """constructor"""
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        """put method"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > super().MAX_ITEMS:
                recent_item = list(self.cache_data.keys())[-2]
                self.cache_data.pop(recent_item)
                print("DISCARD: {}".format(recent_item))

    def get(self, key):
        """get method"""
        if key in self.cache_data.keys():
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key)
