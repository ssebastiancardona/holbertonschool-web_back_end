#!/usr/bin/env python3
""" Paginación hipermedia """
import csv
from typing import List, Tuple, Dict
from math import ceil


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

        rango: Tuple = index_r(page, page_size)
        paginacion: List = self.dataset()

        return (paginacion[rango[0]:rango[1]])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Rango de la página
            Argumentos:
                página: página actual
                page_size: tamaño total de la página
            Regreso:
                Dict con diferentes argumentos
                en el conjunto de datos como un número entero
        """

        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset: List = self.dataset()
        totalpag: int = len(dataset) if dataset else 0
        totalpag = ceil(totalpag / page_size)
        prevpag: int = (page - 1) if (page - 1) >= 1 else None
        nextpag: int = (page + 1) if (page + 1) <= totalpag else None

        hypermedia: Dict = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': nextpag,
            'prev_page': prevpag,
            'total_pages': totalpag,
        }

        return hypermedia


def index_r(page: int, page_size: int) -> Tuple[int, int]:
    """
    Range of the page
    Args:
        page: Current page
        page_size: Total size of the page
    Return:
        tuple with the range start and end size page
    """

    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return (start_size, final_size)