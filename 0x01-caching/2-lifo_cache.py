#!/usr/bin/python3
"""Module documentation
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """Function documentation
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
