import importlib
import argparse
from os import listdir
from os.path import isfile, join
from exception.InvalidCommandException import InvalidCommandException
from constants import COMMAND_PATH

class RSA:
  def __init__(self):
    self.parser = argparse.ArgumentParser(
      description="Outil de génération de clés RSA")

    command = self.parser.add_subparsers(title="Commands", dest="command")

    crypt_parser = command.add_parser("crypt", help="Crypt a message")
    crypt_parser.add_argument("--message", "-m", type=str, help="Message to crypt")

    decrypt_parser = command.add_parser("decrypt", help="Decrypt a message")
    decrypt_parser.add_argument("--message", "-m", type=str, help="Message to decrypt")

    keygen_parser = command.add_parser('keygen', help="Generate RSA Key Pair")
    keygen_parser.add_argument("--size", '-s', type=str, help="Size of the key pair to generate")

    command.add_parser('help', help="Print help")

    self.commands = [f.rstrip(".py") for f in listdir(COMMAND_PATH) if isfile(join(COMMAND_PATH, f))]

  def run(self):
    try:
      args = self.parser.parse_args()
      command = args.command.capitalize() + "Command"
      if command in self.commands:
        module = importlib.import_module("commands." + command)

        if hasattr(module, command):
          MyClass = getattr(module, command)
          instance = MyClass()
          instance.execute(args)
      else:
        raise InvalidCommandException("A Custom Error Was Raised!!!.")
    except InvalidCommandException as e:
      print(self.parser.print_help())


if __name__ == "__main__":
  cli = RSA()
  cli.run()
