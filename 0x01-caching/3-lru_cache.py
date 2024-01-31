#!/usr/bin/python3
"""Module documentation
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """class documentation
    """

    def __init__(self):
        """inti
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """Function documentation
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'. format(discard))

    def get(self, key):
        """Function documentation
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
