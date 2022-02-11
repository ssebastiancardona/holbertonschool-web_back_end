#!/usr/bin/python3
"""module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """clase LFU
    Argumentos:
        BaseCaching (clase): clase básica para esta clase
    """
    def __init__(self):
        """const"""
        super().__init__()
        self.__keys = []
        self.__counter = {}

    def put(self, key, item):
        """poner el elemento en cache_data con el algoritmo LFU
        Argumentos:
            clave ([tipo]): clave del diccionario
            elemento ([tipo]): elemento para insertar en el diccionario
        """
        if not key or not item:
            return
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            self.discard()
        if key not in self.cache_data:
            self.__counter[key] = 1
        else:
            self.__counter[key] += 1
            self.__keys.remove(key)
        self.__keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Obtener el valor del diccionario cache_data
        Argumentos:
            clave ([tipo]): clave para buscar en cache_data
        """
        if not key or key not in self.cache_data:
            return None
        self.__counter[key] += 1
        self.__keys.remove(key)
        self.__keys.append(key)
        return self.cache_data[key]

    def discard(self):
        """descartar elemento e imprimir
        """
        m_time = min(self.__counter.values())
        key = [k for k, v in self.__counter.items() if v == m_time]
        l = 0
        while self.__keys[l] not in key:
            l += 1
        discard = self.__keys.pop(l)
        del self.cache_data[discard]
        del self.__counter[discard]
        print('DISCARD: {}'.format(discard))