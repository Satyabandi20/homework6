import sys
from decimal import Decimal, InvalidOperation
from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand
from calculator.calculator import Calculator
from plugin_loader import load_plugins
from multiprocessing import Process


COMMANDS = {
    'add': AddCommand(),
    'subtract': SubtractCommand(),
    'multiply': MultiplyCommand(),
    'divide': DivideCommand(),
}


load_plugins(COMMANDS)

def perform_command(command_name, args):
    """
    Executes a command from the command dictionary.
    """
    try:
        decimal_args = [Decimal(arg) for arg in args]
        command = COMMANDS.get(command_name)

        if command:
            result = command.execute(*decimal_args)
            print(f"Result: {result}")
        else:
            print(f"Unknown command: {command_name}. Type 'menu' to see available commands.")

    except InvalidOperation:
        print("Error: Invalid number input.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def menu():
    """
    Displays available commands dynamically from the command dictionary.
    """
    print("\nAvailable Commands:")
    for command in COMMANDS:
        print(f"- {command}")
    print("- mp_<command> (Run the command using multiprocessing)")
    print("- menu (to show this menu again)")
    print("- exit (to quit)")

def run_command_in_process(command_name, args):
    """
    Runs a command in a separate process (multiprocessing feature).
    """
    process = Process(target=perform_command, args=(command_name, args))
    process.start()
    process.join()


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


def repl():
    """
    REPL loop to accept user input continuously.
    """
    menu()  # Show menu on start
    while True:
        user_input = input(">>> ").strip().split()

        if not user_input:
            continue

        command_name, *args = user_input

        if command_name.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        elif command_name.lower() == 'menu':
            menu()
        elif command_name.startswith('mp_'):
            # Extract the base command name and run using multiprocessing
            base_command = command_name[3:]
            run_command_in_process(base_command, args)
        else:
            perform_command(command_name, args)

if __name__ == "__main__":
    repl()
