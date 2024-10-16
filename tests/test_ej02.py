from src.Práctica_1_2_Primeros_programa.ej02_def import calcular_importe_trabajado

def test_calcular_importe_trabajado():
    """Test para la función calcular_importe_trabajado"""

    resultado = calcular_importe_trabajado(5, 20)
    assert resultado == "Horas de trabajo: 5\nCoste por hora: 20\nImporte total: 100"

    resultado = calcular_importe_trabajado(0, 30)
    assert resultado == "Horas de trabajo: 0\nCoste por hora: 30\nImporte total: 0"

    resultado = calcular_importe_trabajado(8, 15)
    assert resultado == "Horas de trabajo: 8\nCoste por hora: 15\nImporte total: 120"

    resultado = calcular_importe_trabajado(-1, 15)
    assert resultado == "Horas de trabajo: -1\nCoste por hora: 15\nImporte total: -15"
