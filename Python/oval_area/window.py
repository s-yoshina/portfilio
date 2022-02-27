from tkinter import *
from pathlib import Path
import os

class Window:
    def __init__(self):
        self.root = Tk()
        self.folder_path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.icon_path = self.folder_path / "icon.ico"
        self.window_title = ""

    def set_window_title(self):
        self.root.title(self.window_title)

    def set_icon(self):
        if self.path_validity_check(self.icon_path):
            self.root.iconbitmap(self.folder_path / "icon.ico")
        else:
            self.icon_path = None

    def path_validity_check(self, path):
        if path.exists():
            return True
        return False

if __name__ == '__main__':
    window = Window()
    window.set_window_title()
    window.set_icon()