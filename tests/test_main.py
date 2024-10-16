from src.main import suma

def test_suma():
    assert suma(1, 1) == 2
    assert suma(0, 0) == 0
    assert suma(100, -100) == 0
