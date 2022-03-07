#!/usr/bin/python3
""" captura
"""
from datetime import datetime
from collections import defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ BaseCache define:
      - sobrescribir las funciones 'put' y 'get' para implementar
      Sistema de almacenamiento en caché MRU
    """
    def __init__(self):
        """ inicializar
        """
        super().__init__()
        self.cache_by_time = {}
        self.cache_by_frequency_use = defaultdict(int)  # >>> Default value: 0

    def put(self, key, item):
        """
        Asigne al diccionario self.cache_data el elemento
        valor de la clave clave
        Si el número de elementos en self.cache_data es mayor
        que BaseCaching.MAX_ITEMS:
        - debe descartar el elemento utilizado más recientemente (algoritmo MRU)
        fact lorem
        - debe imprimir DESECHAR: con la llave descartada y seguida por
        una nueva linea
        """
        if key and item:
            self.cache_by_time[key] = datetime.now()
            self.cache_data[key] = item
            self.cache_by_frequency_use[key] += 1

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Elementos ordenados por frecuencia_usados
                frequency_use_filtered = {}
                for k, v in self.cache_by_frequency_use.items():
                    if k != key:
                        frequency_use_filtered[k] = v
                keys_by_frequency_used = sorted(frequency_use_filtered,
                                                key=frequency_use_filtered.get)
                key_to_delete = keys_by_frequency_used[0]

                # Hay más elementos con la misma frecuencia utilizada?
                contador = frequency_use_filtered[key_to_delete]
                posibles_elements_to_discard_dict = {}
                for k, v in frequency_use_filtered.items():
                    if v == contador:
                        posibles_elements_to_discard_dict[k] = v
                if len(posibles_elements_to_discard_dict) > 1:
                    elements_to_discard_by_time = {}
                    for k, v in self.cache_by_time.items():
                        if k in posibles_elements_to_discard_dict.keys():
                            elements_to_discard_by_time[k] = v

                    elements_by_time = sorted(
                                          elements_to_discard_by_time,
                                          key=elements_to_discard_by_time.get)
                    key_to_delete = elements_by_time[0]

                # Delete element with least_frequency_used
                del self.cache_by_time[key_to_delete]
                del self.cache_data[key_to_delete]
                del self.cache_by_frequency_use[key_to_delete]
                print('DISCARD: {}'.format(key_to_delete))

    def get(self, key):
        """
            Devuelve el valor en self.cache_data vinculado a la clave
        """
        elemento = self.cache_data.get(key)
        if elemento:
            self.cache_by_time[key] = datetime.now()
            self.cache_by_frequency_use[key] += 1
        return elemento
