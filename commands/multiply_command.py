from commands.command import Command
from calculator.calculator import Calculator
from decimal import Decimal

class MultiplyCommand(Command):
    """
    Command to perform multiplication of two numbers.
    """
    def execute(self, *args):
        args = [Decimal(arg) for arg in args]
        return Calculator.multiply(*args)
