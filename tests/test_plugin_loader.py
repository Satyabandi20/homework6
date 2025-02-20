from plugin_loader import load_plugins

def test_plugin_loader():
    """
    Test that plugins load correctly.
    """
    commands = {}
    load_plugins(commands)
    assert len(commands) > 0
