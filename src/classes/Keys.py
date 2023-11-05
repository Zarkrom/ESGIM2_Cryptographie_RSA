from interface.CommandInterface import CommandInterface
from utils.FileManager import FileManager
from utils.utils import generate_keypair


class KeygenCommand(CommandInterface):
  def __init__(self):
    self.name = "keygen"
    self.fileManager = FileManager()

  def execute(self, args):
    size = input("Enter the size of the key (in bits): ") if args.size is None else args.size
    print(f"Generating keypair of size {size} bits")

    public_key, private_key = generate_keypair(int(size))

    self.fileManager.save_key_to_file(private_key, is_private=True)
    self.fileManager.save_key_to_file(public_key, is_private=False)

    print("Keygen command executed")

    return True
