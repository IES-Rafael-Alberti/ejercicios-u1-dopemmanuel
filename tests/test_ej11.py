from src.Práctica_1_2_Primeros_programa.ej11_def import leer_numero

def test_leer_numero():
    assert leer_numero(5) == "La suma de los enteros de 1 a 5 es: 15"
    assert leer_numero(10) == "La suma de los enteros de 1 a 10 es: 55"
    assert leer_numero(1) == "La suma de los enteros de 1 a 1 es: 1"
    assert leer_numero(0) == "La suma de los enteros de 1 a 0 es: 0"