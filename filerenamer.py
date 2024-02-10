import os
import tkinter as tk
from tkinter import filedialog

def rename_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".vid"):
            base = os.path.splitext(filename)[0]
            old_name = os.path.join(directory_path, filename)
            new_name = os.path.join(directory_path, base + ".mp4")
            os.rename(old_name, new_name)
            print(f'Renamed: {old_name} to {new_name}')

def select_directory():
    root = tk.Tk()
    root.withdraw() # Hide the main window
    directory_path = filedialog.askdirectory() # Show the directory selection dialog
    rename_files(directory_path)

select_directory()
