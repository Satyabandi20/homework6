from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand
from decimal import Decimal
import pytest
from commands.command import Command


def test_command_not_implemented():
    command = Command()
    with pytest.raises(NotImplementedError):
        command.execute()


def test_add_command():
    command = AddCommand()
    assert command.execute(Decimal(5), Decimal(3)) == Decimal(8)

def test_subtract_command():
    command = SubtractCommand()
    assert command.execute(Decimal(10), Decimal(4)) == Decimal(6)

def test_multiply_command():
    command = MultiplyCommand()
    assert command.execute(Decimal(6), Decimal(6)) == Decimal(36)

def test_divide_command():
    command = DivideCommand()
    assert command.execute(Decimal(8), Decimal(2)) == Decimal(4)

def test_divide_by_zero():
    command = DivideCommand()
    with pytest.raises(ValueError):
        command.execute(Decimal(5), Decimal(0))
