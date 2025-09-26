from src.calculator.operations import addition, subtraction

def test_addition():
    assert addition(3, 7) == 10

def test_subtraction():
    assert subtraction(10, 3) == 7


