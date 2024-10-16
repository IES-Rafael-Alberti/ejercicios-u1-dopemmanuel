from src.Práctica_1_2_Primeros_programa.ej04_def import calculo_grados

def test_calculo_grados():

    assert calculo_grados(12) == "12.00°C en Fahrenheit son °F 53.60"

    assert calculo_grados(-122) == "-122.00°C en Fahrenheit son °F -187.60"

    assert calculo_grados(300) == "300.00°C en Fahrenheit son °F 572.00"
