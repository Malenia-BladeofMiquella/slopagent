# test_calculator.py
from pkg.calculator import Calculator

def test_expression():
    calc = Calculator()
    result = calc.evaluate("3 + 7 * 2")
    print(f"Result: {result}")

test_expression()