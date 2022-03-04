=Mad Libs=
A program where you can play mad libs. The program gets the mad lib from a text file and asks the user to
input words to complete the mad lib. The program will not work without "madlibs.txt".

<madlibs.txt>
This file contains the mad lib. The mad lib within this file can be edited to ask a different mad lib.
To create a mad lib compatible with the program, insert a blank in the mad lib using one of the appropriate words: NOUN, VERB, ADJECTIVE.
The appropriate words have to be capitalized.

Example: I VERB to the station. However, a ADJECTIVE NOUN blocked my path.
There are three blanks in this example: VERB, ADJECTIVE, and NOUN.

<How to play>

1. Input a noun(s), verb(s), or adjective(s) according the prompt of the program.

    - If the program asks for more than one word, seperate the words using a comma.

2. Once all inputs are done, the program will display the mad lib.

3. The user can save the mad lib if desired.

    - The mad lib will be saved to a file called "madlibs_filled.txt".

    - If the file exists, you can either overwrite the file or create a new file.

        - The newly created file will named as a numbered version of the original save file name.
          Ex. "madlibs_filled(1).txt"