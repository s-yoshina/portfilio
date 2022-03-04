import re, os
from pathlib import Path

class MadLibs:
    def __init__(self):
        self.folder_path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.madlib_path = self.folder_path / "madlibs.txt"
        self.check_path_validity(self.madlib_path)
        self.sub_regex = re.compile('NOUN|VERB|ADJECTIVE')
        self.file_content = ""
        self.save_file_name = "madlibs_filled.txt"

    def check_path_validity(self, path):
        """ Checks if a given path is valid."""
        if path.exists() is False:
            print(path)
            raise RuntimeError(f"{path.name} was not found.")

    def main(self):
        print("=Mad Libs=")
        self.obtain_file_content()
        self.enter_words()
        input(self.file_content + "↲")
        self.save_madlib()

    def obtain_file_content(self):
        """ Get the contents of the file containing the madlib."""
        with open(self.madlib_path, mode="r") as f:
            self.file_content = f.read()

    def get_word_counts(self, sub_list) -> tuple:
        """ Gets the number of nouns, verbs, and adjectives in the madlib."""
        n_nouns = sub_list.count("NOUN")
        n_verbs = sub_list.count("VERB")
        n_adjs = sub_list.count("ADJECTIVE")
        return n_nouns, n_verbs, n_adjs

    def get_sub_words(self, n_words, word_type) -> list:
        """ Gets the words to substitute for the word type from input."""
        if n_words == 0: # If there are no words to substitute
            return []
        while True:
            sub_words = input(f"Enter {n_words} {word_type}(s) seperated by commas: \n").split(",")
            sub_words = [word.strip() for word in sub_words]
            if sub_words.count("") > 0: # If a blank was found.
                print("Blank word found. Please enter a word.")
                continue
            if len(sub_words) < n_words:
                print("Not enough words entered.")
                continue
            elif len(sub_words) > n_words:
                print("Too many words entered.")
                continue
            break
        return sub_words

    def insert_sub_words(self, sub_words, word_type):
        """ Inserts words into the madlib."""
        sub_regex = re.compile(f"{word_type}")
        for word in sub_words:
            self.file_content = sub_regex.sub(word, self.file_content, count = 1)

    def enter_words(self):
        """ Substitutes the words in the madlib."""
        word_types = ["noun", "verb", "adjective"]
        sub_list = self.sub_regex.findall(self.file_content)
        n_words = self.get_word_counts(sub_list)
        for word_count, word_type in zip(n_words, word_types):
            sub_words = self.get_sub_words(word_count, word_type)
            self.insert_sub_words(sub_words, word_type.upper())

    def yes_no_prompt(self, message):
        """ Get a yes or no input from the user."""
        while True:
            answer = input(f"{message} (y/n)\n").strip().lower()
            if answer in ("y", "n"):
                return answer
            else:
                print("Invalid input")

    def write_to_file(self, save_file):
        """ Writes the contents of the mad lib a text file."""
        with open(save_file, "w") as f:
            f.write(self.file_content)
        print(f"Mad Lib saved to {save_file.name}")

    def get_largest_file_number(self, file_paths) -> int:
        """Returns the largest numeral of the save files."""
        file_paths.sort()
        file_number_regex = re.compile('madlibs_filled\((\d+)\).txt')
        mo = file_number_regex.search(file_paths[-1].name)
        if mo is None:
            return 1
        return int(mo.group(1))+1

    def create_numbered_file(self):
        """Creates a numbered version of the save file."""
        file_paths = list(self.folder_path.glob('madlibs_filled(*).txt'))
        if len(file_paths) == 0:
            self.write_to_file(self.folder_path / "madlibs_filled(1).txt")
            return
        file_number = self.get_largest_file_number(file_paths)
        self.write_to_file(self.folder_path / f"madlibs_filled({file_number}).txt")

    def save_madlib(self):
        """Saves the madlib to a text file if desired by the player."""
        prompt = "Would you like to save the madlib?"
        if self.yes_no_prompt(prompt) == "y":
            save_file = self.folder_path / self.save_file_name
            if save_file.exists():
                prompt = f"{save_file.name} exists. Would you like to overwrite this file?"
                if self.yes_no_prompt(prompt) == "yes":
                    self.write_to_file(save_file)
                else:
                    self.create_numbered_file()
            else:
                self.write_to_file(save_file)

if __name__ == "__main__":
    madlibs = MadLibs()
    madlibs.main()