#!/usr/bin/python3
"""LIFOCache
module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class
    Args:
        BaseCaching (class):
        Basic class for this class
    """

    def __init__(self):
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """poner elemento en cache_data con algoritmo LIFO
        Argumentos:
            clave ([tipo]): clave del diccionario
            elemento ([tipo]): elemento para insertar en el diccionario
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            disca = self.__keys.pop()
            del self.cache_data[disca]
            print('DISCARD: {}'.format(disca))
        if key and item:
            self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Obtener el valor del diccionario cache_data
        Argumentos:
            clave ([tipo]): clave para buscar en cache_data
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
