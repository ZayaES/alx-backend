#!/usr/bin/env python3
""" implements basic caching"""
from typing import Dict, Any


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class that hold required module for basic caching"""

    def __init__(self):
        """ initiializes instance"""

        super().__init__()

    def put(self, key: Any, item: Any):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """returns the value for the key"""

        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data[key]
