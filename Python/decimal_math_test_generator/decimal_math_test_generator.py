from random import randint, shuffle
import os

class MathTestGenerator:
    ADD_MINUS_MAX_VALUE = 40
    TIMES_V1_MAX = 600
    TIMES_V2_MAX = 9
    MAX_DECIMAL_POINTS = 2

    def __init__(self, n_add_p=0, n_minus_p=0, n_times_p=0, n_divide_p=0):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.problems = []
        self.answers = []
        self.n_add_p = n_add_p
        self.n_minus_p = n_minus_p
        self.n_times_p = n_times_p
        self.n_divide_p = n_divide_p
        self.p_file_name = "problems.txt"
        self.a_file_name = "answers.txt"

    def add_decimal_values(self, value:float, decimal_points:int, ref_value) -> float:
        """Add the decimal values to a value according to the number of decimal points given."""
        divisor = 10
        for i in range(decimal_points):
            decimal_value = float(randint(0,9)/divisor)
            value += decimal_value
            divisor *= 10
        return round(value, decimal_points)

    def generate_value(self, decimal_points:int, max_value, ref_value=0) -> float:
        """Returns the value for the problem."""
        value = float(randint(int(ref_value),int(max_value)))
        return self.add_decimal_values(value, decimal_points, ref_value)

    def round_answer(self, answer, sig_fig):
        """Rounds answers according to their significant figures"""
        if len(str(answer))-1 <= sig_fig:
            return answer
        return float(str(answer)[:sig_fig+1])

    def store_answer(self, value1:float, value2:float, symbol:str):
        """Stores the answer to a problem in a list."""
        sig_fig = min(len(str(value1)), len(str(value2)))-1
        if symbol == "+":
            answer = value1+value2
        elif symbol == "-":
            answer = value1-value2
        elif symbol == "/":
            answer = value1/value2
        else:
            answer = value1*value2
        self.answers.append(self.round_answer(answer, sig_fig))

    def generate_problems_answers(self, symbol):
        """Generates the problems for the quiz"""
        n_decimals_1 = randint(0,self.MAX_DECIMAL_POINTS)
        n_decimals_2 = randint(0,self.MAX_DECIMAL_POINTS)
        if symbol in ("-","+"):
            value1 = self.generate_value(n_decimals_1, self.ADD_MINUS_MAX_VALUE)
            if symbol == "-":
                value2 = self.generate_value(n_decimals_2, value1-1)
            else:
                value2 = self.generate_value(n_decimals_2, self.ADD_MINUS_MAX_VALUE)
        if symbol in ("/", "*"):
            value1 = self.generate_value(n_decimals_1, self.TIMES_V1_MAX)
            if symbol == "/":
                value2 = self.generate_value(n_decimals_2, self.TIMES_V2_MAX, 1)
            else:
                value2 = self.generate_value(n_decimals_2, self.TIMES_V2_MAX)
        self.problems.append(f"{value1} {symbol} {value2} =")
        self.store_answer(value1, value2, symbol)

    def generate_shuffled_problems(self):
        """Generates the problems in a random order."""
        order = (["+"]*self.n_add_p +
                 ["-"]*self.n_minus_p +
                 ["*"]*self.n_times_p +
                 ["/"]*self.n_divide_p)
        shuffle(order)
        [self.generate_problems_answers(symbol) for symbol in order]

    def save_problems(self):
        """Saves the problems to a text file."""
        with open(self.p_file_name, mode ='w') as file:
            for i, problem in enumerate(self.problems):
                if i == len(self.problems)-1:
                    file.write("(%s) %s" % (i+1, problem))
                else:
                    file.write("(%s) %s\n" % (i+1, problem))

    def save_answers(self):
        """Saves the answers to a text file."""
        with open(self.a_file_name, mode ='w') as file:
            for i, answer in enumerate(self.answers):
                if i == len(self.answers)-1:
                    file.write("(%s) %s" % (i+1, answer))
                else:
                    file.write("(%s) %s\n" % (i+1, answer))

    def display_problems(self):
        """Prints the problems"""
        for i, problem in enumerate(self.problems):
            print(f"{i+1}. {problem}")

    def display_answers(self):
        """Prints the answers"""
        for i, answer in enumerate(self.answers):
            print(f"{i+1}. {answer}")

    def display_p_and_a(self):
        """Prints the problems with the answers"""
        for i, problem in enumerate(self.problems):
            print(f"{i+1}. {problem} = {self.answers[i]}")

if __name__ == "__main__":
    mtg = MathTestGenerator(5,5,5,5)
    mtg.generate_shuffled_problems()
    mtg.display_p_and_a()
    mtg.save_problems()
    mtg.save_answers()
