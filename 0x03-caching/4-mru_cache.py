#!/usr/bin/env python3
""" MRU cachine module. """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Inherits from BaseCaching class and is a basic Cache system. """
    order = 0
    ord_d = {}

    def __init__(self):
        """ Constructor of the class. """
        super().__init__()

    def put(self, key, item):
        """ Assigns the item and key to the dictionary cache. """
        if key and item:

            self.cache_data[str(key)] = item
            self.ord_d[str(key)] = {
                "order": self.order,
                "value": item,
            }

            self.order += 1

            if len(self.ord_d) > self.MAX_ITEMS:

                # Obtain most accessed value with order. ━━━━━━━━━━━━━━━━━━━━━━
                max_value = max([
                    dictionary["order"]
                    for dictionary
                    in list(self.ord_d.values())
                ])

                for key, value in self.ord_d.items():
                    if value["order"] == max_value - 1:
                        key_to_pop = key
                print("DISCARD: {}".format(key_to_pop))
                self.ord_d.pop(key_to_pop)
                self.cache_data.pop(key_to_pop)
            # print(self.ord_d)

    def get(self, key):
        """ Returns the value of the cache_data dictionary given its key. """
        if key and key in self.cache_data.keys():
            self.ord_d[str(key)]["order"] = self.order
            self.order += 1
            return(self.cache_data[key])
        return(None)
