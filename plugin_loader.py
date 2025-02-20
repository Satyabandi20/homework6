import os
import importlib

def load_plugins(command_dict):
    plugins_folder = 'plugins'
    for filename in os.listdir(plugins_folder):
        if filename.endswith('.py'):
            module_name = filename[:-3]
            module = importlib.import_module(f'plugins.{module_name}')
            command_class = getattr(module, 'Command', None)
            if command_class:
                command_instance = command_class()
                command_dict[module_name] = command_instance
