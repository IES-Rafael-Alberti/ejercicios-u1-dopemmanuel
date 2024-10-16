from src.Práctica_1_2_Primeros_programa.ej01_def import ask_name

def test_ask_name():
    """Dockstring: Testing T funcion"""

    assert ask_name("Juan") == "Juan"
    assert ask_name("Junior") == "Junior"
