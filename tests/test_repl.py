from main import menu, perform_command
from decimal import Decimal
import pytest

def test_menu(capsys):
    """
    Test the menu output.
    """
    menu()
    captured = capsys.readouterr()
    assert "Available Commands:" in captured.out
    assert "- add" in captured.out
    assert "- subtract" in captured.out

def test_perform_unknown_command(capsys):
    """
    Test unknown command handling.
    """
    perform_command('unknown', [])
    captured = capsys.readouterr()
    assert "Unknown command" in captured.out
