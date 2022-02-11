#!/usr/bin/env python3
"""función auxiliar """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """devuelve una tupla de tamaño dos que contiene un índice inicial y un índice final
    Argumentos:
        página (int): número de página
        page_size (int): tamaño de la página
    Devoluciones:
        Tupla[int, int]: (índice inicial, índice final)
    """
    end: int = page * page_size
    start: int = 0
    for _ in range(page - 1):
        start += page_size
    return (start, end)
