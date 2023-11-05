import base64
from interface.CommandInterface import CommandInterface
from utils.FileManager import FileManager


class DecryptCommand(CommandInterface):
  def __init__(self):
    self.name = "decrypt"
    self.fileManager = FileManager()

  def execute(self, args):
    encrypted_text = input("Enter the encrypted message: ") if args.message is None else args.message

    n, d = self.fileManager.load_key(is_private=True)
    encrypted_blocks = base64.b64decode(encrypted_text.encode()).decode('ascii')
    encrypted_blocks = list(map(int, encrypted_blocks.strip('[]').split(', ')))
    decrypted_blocks = [pow(block, d, n) for block in encrypted_blocks]
    print(''.join([chr(block) for block in decrypted_blocks]))

    return True
