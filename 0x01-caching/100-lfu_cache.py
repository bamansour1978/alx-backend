#!/usr/bin/python3
"""Module documentation
"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """class documentation
    """

    def __init__(self):
        """inti
        """
        super().__init__()
        self.usedKeys = []
        self.frequency = {}

    def put(self, key, item):
        """Function documentation
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lfu = min(self.frequency.values())
                lfu_keys = []
                for k, v in self.frequency.items():
                    if v == lfu:
                        lfu_keys.append(k)
                if len(lfu_keys) > 1:
                    lru_lfu = {}
                    for k in lfu_keys:
                        lru_lfu[k] = self.usedKeys.index(k)
                    discard = min(lru_lfu.values())
                    discard = self.usedKeys[discard]
                else:
                    discard = lfu_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usedKeys[self.usedKeys.index(discard)]
                del self.frequency[discard]
            # update usage frequency
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.usedKeys:
                del self.usedKeys[self.usedKeys.index(key)]
            self.usedKeys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Function documentation
        """
        if key is not None and key in self.cache_data.keys():
            del self.usedKeys[self.usedKeys.index(key)]
            self.usedKeys.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
