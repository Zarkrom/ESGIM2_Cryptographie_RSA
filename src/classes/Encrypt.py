import base64
from interface.CommandInterface import CommandInterface
from utils.FileManager import FileManager


class CryptCommand(CommandInterface):
  def __init__(self):
    self.name = "crypt"
    self.fileManager = FileManager()

  def execute(self, args):
    message = input("Enter the message to encrypt: ") if args.message is None else args.message

    n, e = self.fileManager.load_key(is_private=False)
    numeric_message = [ord(char) for char in message]
    encrypted_blocks = []
    for char_code in numeric_message:
      encrypted_blocks.append(pow(char_code, e, n))

    print(base64.b64encode(str(encrypted_blocks).encode('ascii')).decode())
    return True
