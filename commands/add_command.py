from commands.command import Command
from calculator.calculator import Calculator

class AddCommand(Command):
    def execute(self, *args):
        return Calculator.add(*args)
