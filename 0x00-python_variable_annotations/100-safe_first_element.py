#!/usr/bin/env python3
'''10 safeFirst '''

# No se conocen los tipos de los elementos de la entrada.

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Function
    :)'''
    if lst:
        return lst[0]
    else:
        return None
