from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    """
    Generates test data for arithmetic operations.
    """
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for index in range(num_records):
        operand1 = Decimal(fake.random_number(digits=2))
        operand2 = Decimal(fake.random_number(digits=2))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_function = operation_mappings[operation_name]
        
        if operation_function == divide and operand2 == Decimal('0'):
            expected_result = "ZeroDivisionError"
        else:
            try:
                expected_result = operation_function(operand1, operand2)
            except ZeroDivisionError:
                expected_result = "ZeroDivisionError"

        yield operand1, operand2, operation_name, operation_function, expected_result
