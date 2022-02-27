from tkinter import *
from tkinter import messagebox
from pathlib import Path
from PIL import ImageTk, Image
import os

class ImageViewer:
    FONT_INFO = (15)

    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.folder_path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.image_folder_path = self.folder_path / "images"
        self.check_image_folder_path_validity()
        self.icon_path = self.folder_path / "icon.ico"
        self.check_icon_path_validity()
        self.image_path = ""
        self.image_index = 0
        self.image = None
        self.image_label = None
        self.image_name_label = None
        self.status_label = None
        self.n_images = 0
        self.buttons = {}

        self.main()

    def no_image_folder_error(self):
        messagebox.showerror("Error!", "'images' folder not found.")
        self.root.destroy()
        raise RuntimeError("'images' folder not found.")

    def check_image_folder_path_validity(self):
        if not os.path.isdir(self.image_folder_path):
            self.no_images_error()

    def no_icon_warning(self):
        messagebox.showwarning("Warning", "Icon can not be found.")
        self.icon_path = None

    def check_icon_path_validity(self):
        if self.icon_path.exists() is False:
            self.no_icon_error()

    def main(self):
        #self.resize_window()
        self.set_window_title()
        self.set_icon()
        self.display_image()
        self.display_image_name()
        self.display_buttons()
        self.display_status_label()
        self.root.mainloop()

    def resize_window(self):
        height, width = self.find_largest_image_dimensions()
        height += 200
        width += 200
        self.root.geometry(f"{width}x{height}")

    def set_window_title(self):
        self.root.title("Image Viewer")

    def set_icon(self):
        if self.icon_path is not None:
            self.root.iconbitmap(self.folder_path / "icon.ico")

    def find_largest_image_dimensions(self):
        dimensions = [0,0]
        image_paths = list(self.image_folder_path.glob('*.jpg'))
        image_paths += list(self.image_folder_path.glob('*.png'))
        for path in image_paths:
            with Image.open(path) as im:
                if im.height > dimensions[0]:
                    dimensions[0] = im.height
                if im.width > dimensions[1]:
                    dimensions[1] = im.width
        return dimensions

    def display_image(self):
        height, width = self.find_largest_image_dimensions()
        self.define_image_path()
        with Image.open(self.image_path) as im:
            self.image = ImageTk.PhotoImage(im)
        self.image_label = Label(image=self.image, width=width+10, height=height+10)
        self.image_label.grid(row=0, column=0, columnspan=3)

    def no_images_error(self):
        messagebox.showerror("Error!", "No images found in 'images' folder.")
        self.root.destroy()
        raise RuntimeError("No images found in 'images' folder")

    def define_image_path(self):
        image_paths = list(self.image_folder_path.glob('*.jpg'))
        image_paths += list(self.image_folder_path.glob('*.png'))
        if len(image_paths) == 0:
            self.no_images_error()
        self.image_path = image_paths[self.image_index]

    def display_image_name(self):
        self.image_name_label = Label(self.root, text=self.image_path.name, pady=10, anchor="center", font=(10), bd=1,)
        self.image_name_label.grid(row=1,column=0, columnspan=3)

    def display_buttons(self):
        self.define_buttons()
        self.position_buttons()

    def define_buttons(self):
        self.buttons["back"] = Button(self.root, padx=20, pady=10, text="<<", command=self.scroll_back, font=self.FONT_INFO)
        self.buttons["forward"] = Button(self.root, padx=20, pady=10, text=">>", command=self.scroll_forward, font=self.FONT_INFO)
        self.buttons["exit"] = Button(self.root, padx=50, pady=10, text="Exit Program", command=self.root.destroy, font=self.FONT_INFO)

    def position_buttons(self):
        self.buttons["back"].grid(row=2, column=0)
        self.buttons["exit"].grid(row=2, column=1)
        self.buttons["forward"].grid(row=2, column=2, pady=10)

    def scroll_forward(self):
        self.define_n_images()
        self.image_index = 0 if self.image_index >= self.n_images-1 else self.image_index+1
        self.display_image()
        self.display_image_name()
        self.display_status_label()

    def define_n_images(self):
        image_paths = list(self.image_folder_path.glob('*.jpg'))
        image_paths += list(self.image_folder_path.glob('*.png'))
        self.n_images = len(image_paths)

    def scroll_back(self):
        self.define_n_images()
        self.image_index = self.n_images-1 if self.image_index-1 < 0 else self.image_index-1
        self.display_image()
        self.display_image_name()
        self.display_status_label()

    def display_status_label(self):
        self.define_n_images()
        self.status_label = Label(self.root, text="Image %s of  %s" % (self.image_index+1,self.n_images), font=self.FONT_INFO,
        bd=1, relief=SUNKEN, anchor=E)
        self.status_label.grid(row=4, column=0, columnspan=3, sticky=W+E)

if __name__ == '__main__':
    image_viewer = ImageViewer()