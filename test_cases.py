import calc

# Test cases for addition


def test_add():
    assert calc.add(10, 5, 3) == 18


# Test cases for subtraction
def test_subtract():
    assert calc.subtract(10, 5) == 5


# Test cases for multiplication
def test_multiplication():
    assert calc.multiply(2, 3, 4) == 24


# Test cases for multiplication
def test_division():
    assert calc.divide(4, 2) == 2


# Test cases for expression evaluation
def test_eval():
    assert calc.evaluate(" 8 * 9 + 8") == 80
