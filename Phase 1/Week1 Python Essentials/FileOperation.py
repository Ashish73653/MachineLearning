# GitHub Copilot
from pathlib import Path
import os

# Base directory: the Week1 folder where this script lives
BASE_DIR = Path(__file__).resolve().parent

# Example file path inside the Week1 folder
example_path = BASE_DIR / "example.txt"

# Writing to example.txt
with example_path.open("w", encoding="utf-8") as f:
  f.write("Hello, World!\n")
  f.write("This is a sample file.\n")

# Reading the file we just created
with example_path.open("r", encoding="utf-8") as f:
  print("File content:")
  print(f.read())

# Appending to example.txt
with example_path.open("a", encoding="utf-8") as f:
  f.write("Appending a new line.\n")

# Reading the updated file
with example_path.open("r", encoding="utf-8") as f:
  print("Updated file content:")
  print(f.read())

# Working with directories (create inside Week1 folder)
new_dir = BASE_DIR / "new_folder"
new_dir.mkdir(parents=True, exist_ok=True)
print("New Directory created using pathlib:", new_dir)

another_dir = BASE_DIR / "another_folder"
another_dir.mkdir(parents=True, exist_ok=True)
print("New Directory created using pathlib:", another_dir)

# Handling file exceptions using a path inside Week1 folder
missing = BASE_DIR / "non_existent_file.txt"
try:
  with missing.open("r", encoding="utf-8") as f:
    data = f.read()
except FileNotFoundError:
  print("Error: The file does not exist.")
except IOError:
  print("Error: An I/O error occurred.")
else:
  print("File read successfully.")
finally:
  print("File operation attempted.")
