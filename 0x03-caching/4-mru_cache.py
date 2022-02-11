#!/usr/bin/python3
""" module
cache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """module 
    Args:
        l
    """
    def __init__(self):
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """poner el elemento en cache_data con el algoritmo MRU
        Argumentos:
            clave ([tipo]): clave del diccionario
            elemento ([tipo]): elemento para insertar en el diccionario
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            dis = self.__keys.pop()
            del self.cache_data[dis]
            print('DISCARD: {}'.format(dis))
        if key and item:
            if key not in self.__keys:
                self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """poner el elemento en cache_data con el algoritmo MRU
        Argumentos:
            clave ([tipo]): clave del diccionario
            elemento ([tipo]): elemento para insertar en el diccionario
        """
        if not key or key not in self.cache_data:
            return None
        self.__keys.remove(key)
        self.__keys.append(key)
        return self.cache_data[key]