#!/usr/bin/python3
"""FIFOCache
modulo
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Clase FIFOCache
    Argumentos:
        BaseCaching (clase): clase básica para esta clase
    """

    def __init__(self):
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """poner el elemento en cache_data con el algoritmo FIFO
        Argumentos:
            clave ([tipo]): clave del diccionario
            elemento ([tipo]): elemento para insertar en el diccionario
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            discard = self.__keys.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
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