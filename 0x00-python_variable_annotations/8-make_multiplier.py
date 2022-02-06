#!/usr/bin/env python3
'''8 makMult '''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    toma un multiplicador flotante como argumento
    y devuelve una función
    que multiplica un flotante por
    un multiplicador.
    '''
    def mul(x: float) -> float:
        ''':) :)
        :)'''
        return multiplier * x

    return mul
