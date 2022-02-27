from tkinter import *
from pathlib import Path
import os
from window import Window

class OvalArea(Window):
    CANVAS_HEIGHT = 410
    CANVAS_WIDTH = 410
    PI = 3.14
    CM_PER_PIXEL = 0.026

    def __init__(self):
        self.display_window()
        self.folder_path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.icon_path = self.folder_path / "icon.ico"
        self.window_title = "Slider"
        self.vertical_slider = None
        self.horizontal_slider = None
        self.oval_frame = None
        self.canvas = None
        self.oval = None
        self.area_label = None
        self.oval_area = 0

        self.main()

    def main(self):
        self.set_window_title()
        self.set_icon()
        self.display_vertical_slider()
        self.display_horizontal_slider()
        self.display_oval()
        self.display_area_label()
        self.root.mainloop()

    def display_window(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.geometry("500x475")

    def resize_oval(self, event):
        self.canvas.delete(self.oval)
        self.oval = self.canvas.create_oval(5, 5, self.vertical_slider.get()*2, self.horizontal_slider.get()*2, fill="blue")
        self.canvas.pack()
        self.display_area_label()

    def display_vertical_slider(self):
        self.vertical_slider = Scale(self.root, label="a", length=self.CANVAS_HEIGHT, showvalue=0, from_=5, to=self.CANVAS_HEIGHT/2, command=self.resize_oval)
        self.vertical_slider.grid(row=0, column=0)

    def display_horizontal_slider(self):
        self.horizontal_slider = Scale(self.root, label="b", length=self.CANVAS_WIDTH, showvalue=0, from_=5, to=self.CANVAS_WIDTH/2, orient=HORIZONTAL, command=self.resize_oval)
        self.horizontal_slider.grid(row=1,column=1)

    def display_oval(self):
        self.oval_frame = LabelFrame(self.root, height=self.CANVAS_HEIGHT)
        self.oval_frame.grid(row=0, column=1)
        self.canvas = Canvas(self.oval_frame, bg="white", width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        self.oval = self.canvas.create_oval(5, 5, self.vertical_slider.get()*2, self.horizontal_slider.get()*2, fill="blue")
        self.canvas.pack()

    def display_area_label(self):
        self.oval_area = round((self.PI*self.horizontal_slider.get()*self.vertical_slider.get())*(self.CM_PER_PIXEL**2), 2)
        self.area_label = Label(self.root, text= "Area:\n" + str(self.oval_area) + " cm^2", anchor=W, width=9).grid(row=1, column=0, padx=3)

if __name__ == '__main__':
    oval_area = OvalArea()