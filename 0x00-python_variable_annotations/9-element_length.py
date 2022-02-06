#!/usr/bin/env python3
'''9 elemLeng'''

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ retorna el tamaño
    de una lista """
    return [(index, len(index)) for index in lst]
