import os

current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

import shutil

shutil.rmtree('/path/to/directory')  # Delete tree
