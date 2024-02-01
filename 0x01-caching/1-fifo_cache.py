#!/usr/bin/env python3
""" implements fifo caching"""
from typing import Dict, Any


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class that hold required module for FIFO caching"""

    def __init__(self):
        """ initiializes instance"""

        super().__init__()

    def put(self, key: Any, item: Any):
        """ Add an item in the cache
        """
        my_dict = self.cache_data
        if key is None or item is None:
            return
        my_dict[key] = item
        if len(my_dict) > 4:
            first_in = list(my_dict.keys())[0]
            del my_dict[first_in]
            print("DISCARD: {}".format(first_in))

    def get(self, key: Any) -> Any:
        """returns the value for the key"""

        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data[key]
