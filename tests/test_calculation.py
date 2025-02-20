""" 
Calculation Test Module

This module contains unit tests for the Calculation class. It tests the arithmetic operations 
(add, subtract, multiply, divide) using pytest. The tests ensure that the operate method works 
correctly with Decimal inputs and that the string representation of Calculation instances is 
accurate.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("n1, n2, operation, expected", [
    (Decimal('8'), Decimal('4'), add, Decimal('12')),
    (Decimal('3'), Decimal('3'), subtract, Decimal('0')),
    (Decimal('12'), Decimal('3'), divide, Decimal('4')),
    (Decimal('2'), Decimal('3'), multiply, Decimal('6')),
    (Decimal('3.0'), Decimal('2.0'), add, Decimal('5.0'))
])
def test_operate(n1, n2, operation, expected):
    """
    Test the operate method of the Calculation class.

    This test creates an instance of Calculation using the given
    parameters and asserts that the result of the operate method 
    to match with the expected value.

    Args:
        n1 (Decimal): The first operand.
        n2 (Decimal): The second operand.
        operation (Callable): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    calc = Calculation(n1, n2, operation)
    assert calc.operate() == expected, "Operation failed!"

def test_repr():
    """
    Test the string representation of the Calculation class.

    This test creates a Calculation instance and checks that its
    string representation matches the expected format.
    """
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    str_match = "Calculation(2, 2, add)"
    assert repr(calc) == str_match, f"Expected {str_match} not equal to {repr(calc)}."


def test_divide_by_zero():
    """
    Test the condition of division by zero.

    This test creates a Calculation instance with a divisor of zero 
    and asserts that a ValueError is raised with the correct message.

    Args:
        None
    """
    calc = Calculation(Decimal('5'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.operate()

def test_repr():
    calc = Calculation(Decimal('3'), Decimal('2'), subtract)
    assert repr(calc) == "Calculation(3, 2, subtract)"

def test_repr_edge_case():
    """
    Test edge case where the operation function name might not exist.
    """
    calc = Calculation(Decimal('0'), Decimal('0'), lambda a, b: a + b)
    assert "Calculation(0, 0, <lambda>)" in repr(calc)
