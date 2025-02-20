from commands.command import Command
from calculator.calculator import Calculator
from decimal import Decimal

class DivideCommand(Command):
    """
    Command to perform division of two numbers.
    """
    def execute(self, *args):
        args = [Decimal(arg) for arg in args]
        return Calculator.divide(*args)
