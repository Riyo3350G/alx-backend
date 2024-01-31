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
        self.access_counter = 0

    def put(self, key, item):
        """put method"""
        if key and item:
            if (len(self.cache_data) >= super()
                    .MAX_ITEMS and key not in self.cache_data.keys()):
                least_freq = min(self.freq.values())
                least_freq_keys = [k for k, v in self.freq.items()
                                   if v == least_freq]

                least_freq_keys = min(
                    least_freq_keys,
                    key=lambda x: self.freq.get(x, 0)
                )
                self.cache_data.pop(least_freq_keys)
                self.freq.pop(least_freq_keys)
                print("DISCARD: {}".format(least_freq_keys))
            self.cache_data[key] = item
            self.freq[key] = 0

    def get(self, key):
        """get method"""
        if key in self.cache_data.keys():
            self.cache_data.move_to_end(key, last=True)
            self.freq[key] += 1
            return self.cache_data.get(key)
        return None
