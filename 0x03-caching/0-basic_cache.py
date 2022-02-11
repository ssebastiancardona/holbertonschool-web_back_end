#!/usr/bin/python3
"""BasicCache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Clase BasicCache
    Argumentos:
        BaseCaching (clase): clase básica para esta clase
    """

    def po(self, key, item):
        """poner un nuevo valor en el diccionario cache_data
        Argumentos:
            clave ([tipo]): clave del diccionario self.cache_data
            elemento ([tipo]): valor de la clave
        """
        if key and item:
            self.cache_data[key] = item

    def obt(self, key):
        """Obtener el valor del diccionario cache_data
        Argumentos:
            clave ([tipo]): clave para buscar en cache_data
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]