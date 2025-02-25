import os
from PIL import Image

file_paths = [
    "D:\python_lab\MLPR_Lab5\Lab 5-Spring 2025.ipynb",
    "D:\python_lab\MLPR_Lab5\Plaksha_Faculty.jpg",
    "D:\python_lab\MLPR_Lab5\Dr_Shashi_Tharoor (1).jpg",
]


def check_file_exists(file_path):
    if os.path.exists(file_path):
        print(f"File '{file_path}' loaded successfully.")
    else:
        print(f"Error: File '{file_path}' not found.")
        return False
    return True


def check_image(file_path):
    try:
        img = Image.open(file_path)
        img.verify()
        print(f"Image '{file_path}' loaded successfully.")
    except (IOError, SyntaxError) as e:
        print(f"Error: Image '{file_path}' could not be loaded. {e}")
        return False
    return True


all_files_valid = True
for file_path in file_paths:
    if not check_file_exists(file_path):
        all_files_valid = False
    if file_path.endswith((".jpg")):
        if not check_image(file_path):
            all_files_valid = False

if not all_files_valid:
    raise SystemExit("Some files or images could not be loaded properly.")