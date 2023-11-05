from exception.InvalidCommandException import InvalidCommandException
from interface.CommandInterface import CommandInterface


class HelpCommand(CommandInterface):
  def __init__(self):
    self.name = "decrypt"
    
  def execute(self, args):
    raise InvalidCommandException("Help Command Executed")
