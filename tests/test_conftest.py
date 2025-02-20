from tests.utils import generate_test_data
from decimal import Decimal

def test_generate_test_data():
    """
    Test the data generation function.
    """
    test_data = list(generate_test_data(5))
    assert len(test_data) == 5  # Verify the number of records
    for record in test_data:
        operand1, operand2, operation_name, operation_function, expected_result = record
        assert isinstance(operand1, Decimal)
        assert isinstance(operand2, Decimal)
        assert callable(operation_function)

def test_division_by_zero_handling():
    """
    Test if division by zero is correctly handled in test data.
    """
    for record in generate_test_data(10):
        operand1, operand2, operation_name, operation_function, expected_result = record
        if operation_name == 'divide' and operand2 == Decimal('0'):
            assert expected_result == "ZeroDivisionError"
