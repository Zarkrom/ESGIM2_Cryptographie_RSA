import base64
import os
from constants import KEYGEN_PATH, KEYGEN_PRIVATE, KEYGEN_PUBLIC


class FileManager:
  def create_keygen_folder(self):
    if not os.path.exists(KEYGEN_PATH):
      os.makedirs(KEYGEN_PATH)
    f = open(f"{KEYGEN_PATH}/.gitignore", "w")
    f.write("""*\n!.gitignore""")
    f.close()

  def create_keygen_files(self, public_key, private_key):
    self.save_key_to_file(public_key, is_private=False)
    self.save_key_to_file(private_key, is_private=True)

  def save_key_to_file(self, key, is_private):
    self.create_keygen_folder()
    key_filename = os.path.join(KEYGEN_PATH, KEYGEN_PRIVATE if is_private else KEYGEN_PUBLIC)
    data = '\n'.join([hex(component) for component in key])
    with open(key_filename, 'w') as file:
      file.write(("--- BEGIN PRIVATE KEY ---" if is_private else "--- BEGIN PUBLIC KEY ---") + "\n")
      file.write(base64.b64encode(data.encode()).decode())
      file.write("\n--- END KEY---")

  def decompose(self, key_b64):
    elements = base64.b64decode(key_b64).decode('ascii').strip().split('\n')
    n = int(elements[0], 16)
    de = int(elements[1], 16)
    return n, de

  def load_key(self, is_private):
    key_filename = os.path.join(KEYGEN_PATH, KEYGEN_PRIVATE if is_private else KEYGEN_PUBLIC)
    with open(key_filename, 'r') as f:
      line = f.readlines()
      return self.decompose(line[1].strip())
