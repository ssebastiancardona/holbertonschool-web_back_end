#!/usr/bin/env python3
"""función auxiliar sencilla"""
from typing import Tuple


def index_range(pag: int, pag_size: int) -> Tuple[int, int]:
    """devuelve una tupla de tamaño dos que contiene un índice inicial y un índice final
    Argumentos:
        página (int): número de página
        page_size (int): tamaño de la página
    Devoluciones:
        Tupla[int, int]: (índice inicial, índice final)
    """
    end: int = pag * pag_size
    estart: int = 0
    for _ in range(pag - 1):
        estart += pag_size
    return (estart, end)
