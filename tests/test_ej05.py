from src.Práctica_1_2_Primeros_programa.ej05_def import importes

def test_importes():
    assert importes(12.0, 11) == "Su Importe es de 12.0€, El tipo de IVA a aplicar es de 11%, El precio fina del articulo es de 13.32€."

    assert importes(44.0, 30) == "Su Importe es de 44.0€, El tipo de IVA a aplicar es de 30%, El precio fina del articulo es de 57.2€."