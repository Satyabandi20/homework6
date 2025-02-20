from commands.command import Command

class Command(Command):
    def execute(self, *args):
        return "This is a custom plugin command!"
