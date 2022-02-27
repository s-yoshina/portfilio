from tkinter import *
from tkinter import messagebox
from pathlib import Path
import os

class Calculator:
    OPERATIONS = ["+", "-", "*", "/"]
    FONT_INFO = ('MS Gothic', 20)

    def __init__(self):
        self.window = Tk()
        self.buttons = {}
        self.text_box = None
        self.button_command_values = []
        self.image_folder_path = Path(os.path.dirname(os.path.abspath(__file__)))

        self.first_number = 0
        self.second_number = 0
        self.operation = ""
        self.operation_button_pressed = False
        self.main()

    def main(self):
        self.set_window_title()
        self.define_text_box()
        self.position_text_box()
        self.define_buttons()
        self.position_buttons()
        self.display_icon()
        self.window.mainloop()

    def set_window_title(self):
        self.window.title("Calculator")

    def define_text_box(self):
        self.text_box = Entry(self.window, width=20, borderwidth=5, justify = "right", font=self.FONT_INFO)

    def position_text_box(self):
        self.text_box.grid(row=0, column=0, columnspan=4, padx=50, pady=10, ipady = 20)

    def define_buttons(self):
        self.buttons[1] = Button(self.window, text="1", padx=40, pady=20, command=lambda: self.button_click(1), font=self.FONT_INFO)
        self.buttons[2] = Button(self.window, text="2", padx=40, pady=20, command=lambda: self.button_click(2), font=self.FONT_INFO)
        self.buttons[3] = Button(self.window, text="3", padx=40, pady=20, command=lambda: self.button_click(3), font=self.FONT_INFO)
        self.buttons[4] = Button(self.window, text="4", padx=40, pady=20, command=lambda: self.button_click(4), font=self.FONT_INFO)
        self.buttons[5] = Button(self.window, text="5", padx=40, pady=20, command=lambda: self.button_click(5), font=self.FONT_INFO)
        self.buttons[6] = Button(self.window, text="6", padx=40, pady=20, command=lambda: self.button_click(6), font=self.FONT_INFO)
        self.buttons[7] = Button(self.window, text="7", padx=40, pady=20, command=lambda: self.button_click(7), font=self.FONT_INFO)
        self.buttons[8] = Button(self.window, text="8", padx=40, pady=20, command=lambda: self.button_click(8), font=self.FONT_INFO)
        self.buttons[9] = Button(self.window, text="9", padx=40, pady=20, command=lambda: self.button_click(9), font=self.FONT_INFO)
        self.buttons[0] = Button(self.window, text="0", padx=40, pady=20, command=lambda: self.button_click(0), font=self.FONT_INFO)
        self.buttons["+"] = Button(self.window, text="+", padx=40, pady=20, command=lambda: self.button_click("+"), font=self.FONT_INFO)
        self.buttons["-"] = Button(self.window, text="-", padx=40, pady=20, command=lambda: self.button_click("-"), font=self.FONT_INFO)
        self.buttons["*"] = Button(self.window, text="x", padx=40, pady=20, command=lambda: self.button_click("*"), font=self.FONT_INFO)
        self.buttons["/"] = Button(self.window, text="/", padx=40, pady=20, command=lambda: self.button_click("/"), font=self.FONT_INFO)
        self.buttons["="] = Button(self.window, text="=", padx=40, pady=20, command=lambda: self.button_click("="), font=self.FONT_INFO)
        self.buttons["c"] = Button(self.window, text="C", padx=40, pady=20, command=lambda: self.button_click("c"), font=self.FONT_INFO)

    def position_buttons(self):
        button_number = 1
        for row in range(3, 0, -1):
            for column in range(3):
                self.buttons[button_number].grid(row = row, column = column)
                button_number += 1

        self.buttons[0].grid(row=4, column=0)
        self.buttons["="].grid(row=4, column=1)
        self.buttons["/"].grid(row=4, column=2)
        self.buttons["c"].grid(row=1, column=3)
        self.buttons["+"].grid(row=2, column=3)
        self.buttons["-"].grid(row=3, column=3)
        self.buttons["*"].grid(row=4, column=3)

    def button_click(self, input):
        # If the operation buttons are pressed more than once.
        if self.operation_button_pressed and input in self.OPERATIONS:
            self.operation == input
            return

        inputted_number = self.text_box.get()

        if input in self.OPERATIONS and self.operation_button_pressed is False:
            if self.first_number != 0:
                self.equal_operation(inputted_number)
                inputted_number = self.text_box.get()

            self.operation_button_pressed = True
            self.first_number = inputted_number
            self.operation = input
            return

        if input == "=":
            self.equal_operation(inputted_number)
            return

        if input == "c":
            self.text_box.delete(0, END)
            self.first_number = 0
            self.second_number = 0
            return

        if self.operation_button_pressed:
            self.text_box.delete(0, END)
            inputted_number = self.text_box.get()
            self.operation_button_pressed = False

        self.text_box.insert(len(inputted_number), input)

    def equal_operation(self, inputted_number):
        self.text_box.delete(0, END)
        self.second_number = inputted_number
        self.text_box.insert(0, self.return_operation_result())
        self.first_number = 0
        self.second_number = 0
        self.operation = ""

    def error_reset(self):
        self.first_number = 0
        self.second_number = 0
        self.operation = ""
        self.operation_button_pressed = False
        self.text_box.delete(0, END)

    def non_integer_error(self):
        #raise RuntimeError("Non-integer value")
        messagebox.showerror("Error!", "Non-integer value inputted.\nInputs have been reset.")
        self.error_reset()

    def divide_zero_error(self):
        #raise RuntimeError("Cannot divide by zero")
        messagebox.showerror("Error!", "Cannot divide by zero.\nInputs have been reset.")
        self.error_reset()

    def return_operation_result(self):
        try:
            self.first_number = float(self.first_number)
            self.second_number = float(self.second_number)
        except ValueError:
            self.non_integer_error()
            return 0

        if self.operation == "+":
            return self.first_number+self.second_number
        elif self.operation == "-":
            return self.first_number-self.second_number
        elif self.operation == "*":
            return self.first_number*self.second_number
        elif self.operation == "/":
            if self.second_number == 0:
                self.divide_zero_error()
                return 0
            return self.first_number/self.second_number

    def display_icon(self):
        self.window.iconbitmap(self.image_folder_path / "icon.ico")

if __name__ == '__main__':
    calculator = Calculator()