from main import menu, perform_command, run_command_in_process
from decimal import Decimal
from main import perform_command, run_command_in_process, perform_calculation_and_display
from multiprocessing import Process
import pytest

def test_run_command_in_process():
    """
    Test running a command in a separate process.
    """
    process = Process(target=perform_command, args=('add', [Decimal(2), Decimal(3)]))
    process.start()
    process.join()

def test_menu_output(capsys):
    """
    Test if the menu command outputs the available commands.
    """
    menu()
    captured = capsys.readouterr()
    assert "Available Commands:" in captured.out
    assert "- add" in captured.out
    assert "- subtract" in captured.out
    assert "- multiply" in captured.out
    assert "- divide" in captured.out

def test_unknown_command(capsys):
    """
    Test handling of an unknown command.
    """
    perform_command('unknown_command', [])
    captured = capsys.readouterr()
    assert "Unknown command: unknown_command" in captured.out

def test_invalid_number_input(capsys):
    """
    Test invalid number inputs for operations.
    """
    perform_calculation_and_display("abc", "5", "add")
    captured = capsys.readouterr()
    assert "Invalid number input: abc or 5 is not a valid number." in captured.out

def test_unknown_operation(capsys):
    """
    Test unknown operation handling.
    """
    perform_calculation_and_display("5", "3", "power")
    captured = capsys.readouterr()
    assert "Unknown operation: power" in captured.out
