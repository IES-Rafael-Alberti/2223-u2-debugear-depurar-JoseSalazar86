import pytest
from ..src.Ejercicio2_4 import listaOrdenada

def test_listaOrdenada(listaOrden):
    listaOrden[8, 3, 1, 19, 14]
    assert listaOrdenada(listaOrden) == [1, 3, 8, 14, 19]