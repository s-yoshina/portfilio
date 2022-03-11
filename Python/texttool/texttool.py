from pathlib import Path
import os, re

class TextTool:
    MENU_LENGTH = 5

    def __init__(self):
        self.search_folder_path = Path.cwd() / "search"
        self.file_paths = []

    def main(self):
        self._display_intro()
        self._menu()

    def search(self):
        """Searches for the word or regular expression inputted by the user within
        texts files in the 'search' folder and displays the lines at which the word
        was found."""
        search_expression = input("Enter a word or a regular expression to find: ")
        search_regex = re.compile(search_expression)
        print()

        self._display_matches(search_regex)

    def search_replace(self):
        """Searches for the word inputted by the user within
        texts files in the 'search' folder and replaces the word
        with another word inputted by the user."""
        matches = []

        find = input("Enter a word or a regular expression to replace: ")
        find_regex = re.compile(find)

        replace_word = input("Enter the word you would like to replace the above: ")
        self._conduct_replacement(find_regex, replace_word)

    def word_count(self):
        file_text = self._get_file_text()
        file_text = self._generate_word_list(file_text)

        word_count = self._get_word_count(file_text)
        words, count = self._sort_word_count(word_count)

        self._display_top_ten_words(words, count)
        self._specific_word_count(word_count)

    def change_search_directory(self):
        print("The current search directory is\n%s" % (self.search_folder_path))
        path = input("""Please enter the path of the directory you would like to search.
(Enter a blank path to return to the menu)
""")
        if path.strip() != "":
            self.search_folder_path = Path(path)

    def _display_intro(self):
        # Title
        print("*"*14)
        print("  Text Tool")
        print("*"*14)

        # Description
        input("""Description: A small program that allows you to handle text
within text files.↲""")
        print()

    def _menu(self):
        """Main loop for the program"""
        while True:
            self._display_commands_list()

            cmd = self._get_command(list(range(1, self.MENU_LENGTH + 1)))
            if cmd == self.MENU_LENGTH:
                break
            elif cmd == 4:
                self._conduct_operation(cmd)
                continue

            if self._search_folder_path_exists() is False:
                continue
            self._get_text_file_paths()
            if len(self.file_paths) == 0:
                input("No .txt files were found.")
                continue
            self._conduct_operation(cmd)

    def _display_commands_list(self):
        print("Enter a number from the list below")
        print("1. Search")
        print("2. Search & replace")
        print("3. Each word count")
        print("4. Change search directory")
        print("5. Exit program")

    def _get_command(self, options):
        while True:
                cmd = int(input().strip())
                if cmd in options:
                    break
                else:
                    print("Invalid input.")
        return cmd

    def _search_folder_path_exists(self):
        if self.search_folder_path.exists() is False:
            input("The following directory could not be found.\n%s↲" % (self.search_folder_path))
            input("Please change the search directory through the 'Change search directory' option.↲")
            return False
        return True

    def _get_text_file_paths(self):
        self.file_paths = list(self.search_folder_path.glob('*.txt'))

    def _conduct_operation(self, cmd):
        """Conducts operation based on the users input."""
        OPERATION_CMD = {
        1 : self.search,
        2 : self.search_replace,
        3 : self.word_count,
        4 : self.change_search_directory
        }
        OPERATION_CMD[cmd]()

    def _display_matches(self, search_regex):
        """Goes through each text file and displays the line where a match was found."""
        match_count = 0
        for file_path in self.file_paths:
            print("Searching %s..." %(file_path.name))
            with open(file_path, mode = "r") as text_file:
                file_content = text_file.readlines()
                for i in range(len(file_content) - 1):
                    if len(search_regex.findall(file_content[i].lower())) == 0:
                        continue
                    print("L%s: %s" % (i + 1, file_content[i]))
                    match_count += 1
        input("%s matches found.↲" % (match_count)) if (match_count > 0) else input("No matches founds.↲")

    def _conduct_replacement(self, find_regex, replace_word):
        replacement_count = 0

        for file_path in self.file_paths:
            with open(file_path, mode = 'r') as replace_file:
                file_text = replace_file.read()
            replacement_count += len(find_regex.findall(file_text))
            file_text = find_regex.sub(replace_word, file_text)
            with open(file_path, mode = 'w') as replace_file:
                replace_file.write(file_text)

        if replacement_count == 0:
            input("No matches found.↲")
        else:
            input("%s replacements were made.↲" % (replacement_count))

    def _get_file_text(self):
        file_text = ""
        for path in self.file_paths:
            with open(path, mode ='r') as file:
                file_text += file.read() + "\n"
        return file_text

    def _generate_word_list(self, file_text):
        remove_regex = re.compile('[,."():;~/*+]')
        file_text = remove_regex.sub("", file_text)
        file_text = file_text.lower().split()
        return file_text

    def _get_word_count(self, file_text):
        word_count = {}
        for word in file_text:
            if word not in word_count.keys():
                word_count[word] = 1
            else:
                word_count[word] += 1
        return word_count

    def _sort_word_count(self, word_count):
        words = []
        count = []

        for key, value in word_count.items():
            words.append(key)
            count.append(value)

            if len(words) > 1:
                if count[-1] > count[-2]:
                    for i in range(len(words)-1,0,-1):
                        if count[i] > count[i-1]:
                            self._switch_position(words, i)
                            self._switch_position(count, i)
                        else:
                            break
        return words, count

    def _switch_position(self, array, index):
        temp = array[index-1]
        array[index-1] = array[index]
        array[index] = temp

    def _display_top_ten_words(self, words, count):
        """Displays the number of times a word appeared in the files."""
        display_count = 10 if len(words) > 10 else len(words)
        print("\nPrinting the top %s words found in the files." % (display_count))
        for i in range(display_count):
            if i == display_count - 1:
                input("%s: %s↲" % (words[i], count[i]))
            else:
                print("%s: %s" % (words[i], count[i]))

    def _get_user_input(self, options):
        """Gets the menu command from the user."""
        while True:
                cmd = input().strip().lower()
                if cmd in options:
                    break
                else:
                    print("Invalid input.")
        return cmd

    def _specific_word_count(self, word_count):
        while True:
            print("Would you like to know the count for a specific word? (y/n)")
            cmd = self._get_user_input(["y", "n"])

            if cmd == "y":
                self._display_specific_word_count(word_count)
            else:
                break

    def _display_specific_word_count(self, word_count):
        print("Please enter the word you would like to know the count for:")
        word = input().lower()

        if word in word_count.keys():
            input("%s↲" %(word_count[word]))
        else:
            input("Entered word was not found.↲")
            #print("If the word has a '.' in it, please remove the '.' in your input.")

if __name__ == '__main__':
    if Path.cwd() != Path(os.path.abspath(__file__)).parent:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
    text_tool = TextTool()
    text_tool.main()