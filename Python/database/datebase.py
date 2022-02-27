from tkinter import *
from tkinter import messagebox
from pathlib import Path
import os
from window import Window
import sqlite3

class Database(Window):
    def __init__(self):
        self.root = None
        self.folder_path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.icon_path = self.folder_path / "icon.ico"
        self.window_title = "Database"
        self.database_categories = ["first_name", "last_name", "address", "city", "state", "zipcode"]
        self.textbox_label_texts = ["First Name", "Last Name", "Address", "City", "State", "Zipcode"]
        self.connection = None
        self.cursor = None
        self.text_boxes = {}
        self.text_box_labels = {}
        self.buttons = {}
        self.submit_button = None
        self.query_button = None
        self.records = []
        self.retreived_record = []
        self.delete_id = 0

        self.main()

    def main(self):
        self.initialization()
        self.set_window_title()
        self.set_icon()
        self.display_title_label()
        self.display_text_boxes()
        self.display_textbox_labels()
        self.display_buttons()
        self.root.mainloop()

    def initialization(self):
        os.chdir(self.folder_path)
        self.root = Tk()
        self.root.resizable(0,0)
        if self.database_exists() is False:
            self.initialize_database()

    def database_exists(self):
        database_path = self.folder_path / "address_book.db"
        if database_path.is_file():
            return True
        return False

    def initialize_database(self):
        self.connect_to_database()
        self.create_table()
        self.close_connection_to_database()

    def connect_to_database(self):
        self.connection = sqlite3.connect('address_book.db')
        self.cursor = self.connection.cursor()

    def close_connection_to_database(self):
        self.connection.commit()
        self.connection.close()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")

    def display_title_label(self):
        title_label_frame = LabelFrame(self.root)
        title_label_frame.grid(row=0, column=0, columnspan=2, pady=5)
        Label(title_label_frame, text="Address Database").grid(row=0, column=0)

    def display_textbox_labels(self):
        for index, category in enumerate(self.database_categories):
            self.text_box_labels[category] = Label(self.root, text=self.textbox_label_texts[index])
            self.text_box_labels[category].grid(row=index + 1, column=0)
        self.text_box_labels["first_name"].grid(row=1, column=0, padx=5)

    def display_text_boxes(self):
        for index, category in enumerate(self.database_categories):
            self.text_boxes[category] = Entry(self.root, width=30)
            self.text_boxes[category].grid(row=index + 1, column=1, padx=20)
        # pady=(t, b) [t: padding on the top, b: padding on the bottom]
        self.text_boxes["first_name"].grid(row=1, column=1)

    def clear_text_boxes(self):
        for category in self.database_categories:
            self.text_boxes[category].delete(0, END)

    def display_buttons(self):
        self.buttons["submit"] = Button(self.root, text="Submit", command=self.submit_to_database)
        self.buttons["submit"].grid(row=len(self.database_categories) + 1, column=0, columnspan=2, padx=10, pady=5, ipadx=100)

        self.buttons["query"] = Button(self.root, text="Show Records", command=self.query)
        self.buttons["query"].grid(row=len(self.database_categories) + 2, column=0, columnspan=2, padx=10, pady=5, ipadx=85)

        self.buttons["delete"] = Button(self.root, text="Delete Record", command=self.display_delete_window)
        self.buttons["delete"].grid(row=len(self.database_categories) + 3, column=0, columnspan=2, padx=10, pady=5, ipadx=85)

        self.buttons["edit"] = Button(self.root, text="Edit Record", command=self.display_edit_window)
        self.buttons["edit"].grid(row=len(self.database_categories) + 4, column=0, columnspan=2, padx=10, pady=5, ipadx=91)

    def submit_to_database(self):
        self.connect_to_database()
        self.insert_values_into_database()
        self.close_connection_to_database()
        self.clear_text_boxes()

    def insert_values_into_database(self):
        cursor_dictionary = {}
        for category in self.database_categories:
            cursor_dictionary[category] = self.text_boxes[category].get()

        self.cursor.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)", cursor_dictionary)

    def query(self):
        self.connect_to_database()
        self.retreive_data()
        self.close_connection_to_database()
        self.display_records()

    def retreive_data(self):
        self.cursor.execute("SELECT *, oid FROM addresses")
        # Other fetch methods: fetchone(), fetchmany(i) [i: How many values you want to fetch]
        self.records = self.cursor.fetchall()

    # Display Record Window
    def display_records(self):
        self.display_record_window()
        self.display_record_window_row_labels()
        self.display_record_window_label()
        self.display_record_window_close_button()

    def display_record_window(self):
        self.record_window = Toplevel()
        self.record_window.title("Records")
        self.record_window.iconbitmap(self.folder_path / "icon.ico")

    def display_record_window_row_labels(self):
        Label(self.record_window, text="ID", justify="left").grid(row=0, column=0)
        row_text = ""
        for index, text in enumerate(self.textbox_label_texts):
            row_text += "%s\n" % (text)
        Label(self.record_window, text=row_text, justify="left").grid(row=1, column=0, padx=5)

    def display_record_window_label(self):
        for index, record in enumerate(self.records):
            record_text = ""
            for row in range(len(record) - 1):
                record_text += "%s\n" % (record[row])
            Label(self.record_window, text="%s" % (record[-1]), width=5).grid(row=0, column=index+1)
            Label(self.record_window, text=record_text).grid(row=1, column=index+1)

    def display_record_window_close_button(self):
        close_button = Button(self.record_window, text="Close Window", command=self.record_window.destroy)
        close_button.grid(row=2, column=0, columnspan=len(self.records) + 1, pady=(0,5))

    # Delete Window
    def display_delete_window(self):
        self.delete_window = Toplevel()
        self.delete_window.title("Delete Record")
        self.delete_window.iconbitmap(self.folder_path / "icon.ico")
        Label(self.delete_window, text="Enter ID of entry to delete:").grid(row=0, column=0, pady=5)
        self.text_boxes["id"] = Entry(self.delete_window, width=20)
        self.text_boxes["id"].grid(row=1, column=0, pady=5)
        Button(self.delete_window, text="Delete", command=self.delete_record_from_database).grid(row=2, column=0, pady=5)

    def delete_record_from_database(self):
        self.delete_id = self.text_boxes["id"].get()
        if self.check_id_validity(self.delete_id) is False:
            messagebox.showerror("Invalid ID", "ID was not found in the database.")
            return
        self.connect_to_database()
        #WHERE... first_name="name", etc.
        self.cursor.execute("DELETE from addresses WHERE oid=" + self.delete_id)
        self.close_connection_to_database()
        self.delete_window.destroy()

    def check_id_validity(self, id):
        self.connect_to_database()
        self.retreive_data()
        self.close_connection_to_database()
        ids = [str(record[-1]) for record in self.records]
        if id in ids:
            return True
        return False

    # Edit Window
    def display_edit_window(self):
        self.edit_window = Toplevel()
        self.edit_window.title("Edit Record")
        self.edit_window.iconbitmap(self.folder_path / "icon.ico")
        self.display_edit_window_labels()
        self.display_edit_window_textboxes()
        self.display_edit_window_buttons()

    def display_edit_window_labels(self):
        # ID label
        Label(self.edit_window, text="Enter ID of\n record to edit:").grid(row=0, column=0, rowspan=2)

        # Textbox labels
        for index, category in enumerate(self.database_categories):
            Label(self.edit_window, text=self.textbox_label_texts[index]).grid(row=index+2, column=0)

    def display_edit_window_textboxes(self):
        # ID Textbox
        self.text_boxes["edit_id"] = Entry(self.edit_window, width=20)
        self.text_boxes["edit_id"].grid(row=0, column=1, pady=5)

        # Info textboxes
        for index, category in enumerate(self.database_categories):
            category_name = "edit_" + category
            self.text_boxes[category_name] = Entry(self.edit_window, width=30, state=DISABLED)
            self.text_boxes[category_name].grid(row=index+2, column=1, padx=20)

    def display_edit_window_buttons(self):
        self.buttons["edit_window_id"] = Button(self.edit_window, text="Select ID", command=self.retreive_id_data)
        self.buttons["edit_window_id"].grid(row=1, column=1)
        self.buttons["edit_window_edit"] = Button(self.edit_window, text="Edit Record", command=self.edit_record_in_database, state=DISABLED)
        self.buttons["edit_window_edit"].grid(row=len(self.database_categories)+2, column=1)
        self.buttons["edit_window_reset"] = Button(self.edit_window, text="Reset Window", command=self.reset_edit_window)
        self.buttons["edit_window_reset"].grid(row=len(self.database_categories)+2, column=0, padx=10)

    def retreive_id_data(self):
        self.edit_id = self.text_boxes["edit_id"].get()
        if self.check_id_validity(self.edit_id) is False:
            messagebox.showerror("Invalid ID", "ID was not found in the database.")
            return

        self.connect_to_database()

        self.cursor.execute("SELECT * FROM addresses WHERE oid = " + self.edit_id)
        # Other fetch methods: fetchone(), fetchmany(i) [i: How many values you want to fetch]
        self.retreived_record = self.cursor.fetchall()
        self.retreived_record = list(self.retreived_record[0])

        self.close_connection_to_database()
        self.enable_edit_window_textboxes()
        self.display_retreived_data()
        self.buttons["edit_window_edit"]["state"] = "normal"
        self.disable_id_related_widgets()

    def disable_id_related_widgets(self):
        self.text_boxes["edit_id"]["state"] = "disabled"
        self.buttons["edit_window_id"]["state"] = "disabled"

    def display_retreived_data(self):
        for index, category in enumerate(self.database_categories):
            category_name = "edit_" + category
            self.text_boxes[category_name].insert(0, self.retreived_record[index])

    def enable_edit_window_textboxes(self):
        for category in self.database_categories:
            category_name = "edit_" + category
            self.text_boxes[category_name]['state'] = 'normal'

    def edit_record_in_database(self):
        self.connect_to_database()

        cursor_dictionary = {}
        for category in self.database_categories:
            category_name = "edit_" + category
            cursor_dictionary[category] = self.text_boxes[category_name].get()
        cursor_dictionary["oid"] = self.edit_id

        self.cursor.execute("""UPDATE addresses SET
            first_name = :first_name,
            last_name = :last_name,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode

            WHERE oid = :oid""", cursor_dictionary)
        self.close_connection_to_database()

    def reset_edit_window(self):
        self.reset_edit_window_textboxes()
        self.reset_edit_window_buttons()

    def reset_edit_window_buttons(self):
        self.buttons["edit_window_id"]["state"] = "normal"
        self.buttons["edit_window_edit"]["state"] = "disabled"

    def reset_edit_window_textboxes(self):
        self.text_boxes["edit_id"]["state"] = "normal"
        self.text_boxes["edit_id"].delete(0, END)

        for category in self.database_categories:
            category_name = "edit_" + category
            self.text_boxes[category_name].delete(0, END)
            self.text_boxes[category_name]["state"] = "disabled"

if __name__ == '__main__':
    database = Database()