'''
This module contains tests for the `perform_calculation_and_display` function
from the main application. It uses the pytest framework to validate the behavior
of various arithmetic operations, including addition, subtraction, multiplication,
and division. The tests also cover edge cases such as invalid inputs and
unknown operations.
'''
import pytest
from main import perform_calculation_and_display

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Adjusted for the actual error message
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")  # Testing another invalid number input
])
def test_perform_calculation_and_display(a_string, b_string, operation_string,expected_string, capsys):
    '''
    Tests the perform_calculation_and_display function for various inputs.
    '''
    perform_calculation_and_display(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string