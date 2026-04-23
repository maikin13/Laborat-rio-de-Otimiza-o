import pytest
from src import algoritmos

def test_calcular_media():
    assert algoritmos.calcular_media([10.0, 20.0, 30.0]) == 20.0

def test_calcular_desvio_padrao_sucesso():
    resultado = algoritmos.calcular_dp([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0])
    assert round(resultado,2) == 2.14

def test_calcular_euclidiana():
    assert algoritmos.dist_euclidiana([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]) == pytest.approx(5.196, 0.01)

def test_multiplicar_escalar():
    assert algoritmos.multiplicar_escalar([1.0, 2.0, 3.0], 2.0) == [2.0, 4.0, 6.0]