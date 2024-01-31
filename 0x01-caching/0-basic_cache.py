#!/usr/bin/env python3
"""Module documentation
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class documentation
    """

    def __init__(self):
        """inti
        """
        super().__init__()

    def put(self, key, item):
        """Function documentation
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Function documentation
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
