import os
import logging
from decimal import Decimal, InvalidOperation
from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand
from calculator.calculator import Calculator
from plugin_loader import load_plugins
from multiprocessing import Process
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
environment = os.getenv('ENVIRONMENT', 'production')
api_key = os.getenv('API_KEY')

# Configure logging
log_file_path = os.path.join(os.path.dirname(__file__), 'app.log')
logging.basicConfig(
    level=logging.DEBUG if environment == 'development' else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path, mode='a'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info(f"Environment: {environment}")

COMMANDS = {
    'add': AddCommand(),
    'subtract': SubtractCommand(),
    'multiply': MultiplyCommand(),
    'divide': DivideCommand(),
}

load_plugins(COMMANDS)
logger.info("Plugin commands loaded.")

def perform_command(command_name, args):
    """
    Executes a command from the command dictionary.
    """
    try:
        decimal_args = [Decimal(arg) for arg in args]
        command = COMMANDS.get(command_name)

        if command:
            result = command.execute(*decimal_args)
            logger.info(f"Executed {command_name} with arguments {args}, result: {result}")
            print(f"Result: {result}")
        else:
            logger.warning(f"Unknown command: {command_name}")
            print(f"Unknown command: {command_name}. Type 'menu' to see available commands.")

    except InvalidOperation:
        logger.error("Invalid number input.")
        print("Error: Invalid number input.")
    except ZeroDivisionError:
        logger.error("Division by zero is not allowed.")
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        logger.exception(f"An error occurred: {e}")
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
            logger.info(f"Performed {operation_type} on {num1} and {num2}, result: {result}")
            print(f"The result of {num1} {operation_type} {num2} is equal to {result}")
        else:
            logger.warning(f"Unknown operation: {operation_type}")
            print(f"Unknown operation: {operation_type}")
    except InvalidOperation:
        logger.error(f"Invalid number input: {num1} or {num2}")
        print(f"Invalid number input: {num1} or {num2} is not a valid number.")
    except ZeroDivisionError:
        logger.error("Division by zero.")
        print("Error: Division by zero.")
    except Exception as e:
        logger.exception(f"An error occurred: {e}")
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