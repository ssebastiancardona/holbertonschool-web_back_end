#!/usr/bin/env python3
""" Paginación sencilla """
import csv
import math
from typing import List, Tuple


class Server:
    """Clase de servidor para paginar una base de datos de nombres de bebés populares.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Conjunto de
        datos en caché
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Obtener la página
            Argumentos:
                página: página actual
                page_size: tamaño total de la página
            Regreso:
                Lista de la paginación realizada
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range: Tuple = index_range(page, page_size)
        pagination: List = self.dataset()

        return (pagination[range[0]:range[1]])


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Rango de la página
    Argumentos:
        página: página actual
        page_size: tamaño total de la página
    Regreso:
        tupla con la página de tamaño inicial y final del rango
    """

    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return (start_size, final_size)
