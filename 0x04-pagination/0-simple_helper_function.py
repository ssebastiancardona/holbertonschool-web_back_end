#!/usr/bin/env python3
""" Obtiene los índices para la paginación """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Rango de la página
        Argumentos:
            página: página actual
            page_size: tamaño total de la página
        Regreso:
            tupla con la página de tamaño inicial y final del rango
    """

    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return (start_size, final_size)
