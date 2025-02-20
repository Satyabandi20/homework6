from commands.command import Command
from calculator.calculator import Calculator

class SubtractCommand(Command):
    def execute(self, *args):
        return Calculator.subtract(*args)
