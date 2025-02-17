import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def perform_calculation_and_display(num1, num2, operation_type):
    """
    Performs the specified arithmetic operation on two numbers and prints the result.
    """
    operation_functions = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }
    try:
        decimal_num1, decimal_num2 = map(Decimal, [num1, num2])
        operation_function = operation_functions.get(operation_type)
        if operation_function:
            result = operation_function(decimal_num1, decimal_num2)
            print(f"The result of {num1} {operation_type} {num2} is equal to {result}")
        else:
            print(f"Unknown operation: {operation_type}")
    except InvalidOperation:
        print(f"Invalid number input: {num1} or {num2} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")
        

def main():
    """
    Main function to handle command-line arguments and initiate the calculation.
    """
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, num1, num2, operation_type = sys.argv
    perform_calculation_and_display(num1, num2, operation_type)

if __name__ == '__main__':
    main()