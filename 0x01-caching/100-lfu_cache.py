#!/usr/bin/env python3
"""lfu caching module"""
from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """"LFUCache Class"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)
        self.freq = {}

    def put(self, key, item):
        """put method"""
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.freq[key] += 1
                self.cache_data.move_to_end(key, last=True)
            else:
                if len(self.cache_data) >= super().MAX_ITEMS:
                    recent_item = list(self.freq.keys())[0]
                    self.cache_data.pop(recent_item)
                    self.freq.pop(recent_item)
                    print("DISCARD: {}".format(recent_item))
                self.cache_data[key] = item
                self.freq[key] = 1

    def get(self, key):
        """get method"""
        if key in self.cache_data.keys():
            self.freq[key] += 1
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key)
