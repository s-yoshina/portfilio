from window import Window
from tkinter import *
from tkinter import messagebox
from pathlib import Path
import os
from random import randint

class MultiplicatonQuiz(Window):
    N_QUESTIONS = 10

    def __init__(self):
        self.root = Tk()
        self.top_level = None
        self.folder_path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.icon_path = self.folder_path / "icon.ico"
        self.window_title = "Multiplication Quiz"
        self.question = "Click the 'Start' button\n to begin the quiz."
        self.question_number = 1
        self.correct_answers = 0
        self.answer = None

        # Frame
        self.title_frame = None
        # Labels
        self.title_label = None
        self.question_label = None
        # Textbox
        self.answer_box = None
        # Buttons
        self.answer_button = None
        self.start_button = None
        # Messagebox
        self.messagebox = None

        self.display_window()
        self.root.bind("<Return>", self.return_event)
        self.root.mainloop()

    def return_event(self, event):
        """Event for the 'Enter' key."""
        if self.start_button["state"] == "normal":
            self.start_quiz()
            return

        if self.answer_button["state"] == "normal":
            self.answer_question()

    def display_title(self):
        """Displays the title of the application."""
        self.title_frame = LabelFrame(self.root)
        self.title_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.title_label = Label(self.title_frame, text="Multiplication Quiz", font=20)
        self.title_label.pack()

    def create_question_label(self):
        self.question_label = Label(self.root, text=self.question, font=10)
        self.question_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def create_answer_box(self):
        self.answer_box = Entry(self.root, justify="center", borderwidth=2, font=10, state=DISABLED)
        self.answer_box.grid(row=2, column=0, padx=10, pady=5)

    def generate_q_and_a(self):
        """Creates the question and stores the answer to the question."""
        n1, n2 = randint(0,9), randint(0,9)
        self.question = f"Q{self.question_number}: {n1} x {n2} = ?"
        self.answer =  n1*n2

    def display_new_question(self):
        self.generate_q_and_a()
        self.question_label["text"] = self.question

    def display_results(self):
        """Displays the users score on the quiz."""
        messagebox_text = f"You got {self.correct_answers}/{MultiplicatonQuiz.N_QUESTIONS} correct!"
        self.messagebox = messagebox.showinfo("Result", messagebox_text)

    def reset_state(self):
        """Resets the state of the program."""
        self.correct_answers = 0
        self.question_number = 1
        self.question_label["text"] = "Click the 'Start' button\n to begin the quiz."
        self.start_button["state"] = "normal"

    def end_quiz(self):
        """Displays the results and returns the program to its initial state."""
        self.answer_button["state"] = "disabled"
        self.answer_box["state"] = "disabled"
        self.display_results()
        self.reset_state()

    def answer_question(self):
        """Gets the user input and sees whether the user got the right answer or not.
        If all questions are answered, the method ends the quiz. If not, a new question is displayed."""
        player_answer = self.answer_box.get().strip()
        if player_answer == str(self.answer):
            self.correct_answers += 1
        self.answer_box.delete(0, END)
        if self.question_number == MultiplicatonQuiz.N_QUESTIONS:
            self.end_quiz()
        else:
            self.question_number += 1
            self.display_new_question()

    def create_answer_button(self):
        self.answer_button = Button(self.root, text="Answer", font=10,
                                    command=self.answer_question, state=DISABLED)
        self.answer_button.grid(row=2, column=1, padx=5, pady=5)

    def start_quiz(self):
        self.start_button["state"] = "disabled"
        self.answer_button["state"] = "normal"
        self.answer_box["state"] = "normal"
        self.display_new_question()

    def create_start_button(self):
        self.start_button = Button(self.root, text="Start", width=20, font=10, command=self.start_quiz)
        self.start_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def display_window(self):
        self.set_window_title()
        self.set_icon()
        self.display_title()
        self.create_question_label()
        self.create_answer_box()
        self.create_answer_button()
        self.create_start_button()

if __name__ == "__main__":
    multiplication_quiz = MultiplicatonQuiz()