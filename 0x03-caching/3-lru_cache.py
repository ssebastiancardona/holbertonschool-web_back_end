#!/usr/bin/env python3
"""
Module :)
"""
from collections import deque

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Define una clase
    """
    def __init__(self):
        super().__init__()
        self.__queue = deque()

    def put(self, key, item):
        """
        asignacion de digccionario
        """
        if key and item:
            if key in self.cache_data:
                self.__queue.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard(key)

            self.__queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        retorna el valor
        """
        if key in self.cache_data:
            self.__queue.remove(key)
            self.__queue.append(key)
            return self.cache_data.get(key)
        return None

    def discard(self, key):
        """
        descart
        """
        remov = self.__queue.popleft()
        del self.cache_data[remov]
        print(f"DISCARD: {remov}")