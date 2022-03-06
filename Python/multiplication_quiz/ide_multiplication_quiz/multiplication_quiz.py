import random, time

class MultiplicationQuiz:
    NTRIES = 3 # Number of tries per question
    TIMEPERQ = 8  # Number of seconds given per question
    NQUESTIONS = 10 # Number of questions asked

    def __init__(self):
        self.n_correct = 0

    def main(self):
        self.print_title()
        self.start_quiz()
        self.display_result()

    def print_title(self):
        """Displays the title of the program"""
        input('''Press "Enter" to start the multiplication quiz (%s Question(s)).
Time limit per question: %s seconds
Attempts per problem: %s↲''' % (MultiplicationQuiz.NQUESTIONS,
                               MultiplicationQuiz.TIMEPERQ,
                               MultiplicationQuiz.NTRIES))

    def incorrect(self, number1, number2, startingtime) -> int:
        """Returns whether the user got the answer right after getting the question wrong
       on the first try."""
        anw = ''
        CurrentAttempts = 1
        while anw != number1*number2 and CurrentAttempts < MultiplicationQuiz.NTRIES:
            try:
                anw = int(input("%s attempt(s) left.\n" % (MultiplicationQuiz.NTRIES - CurrentAttempts)))
                endingtime = time.time() - startingtime
                if endingtime >= MultiplicationQuiz.TIMEPERQ:
                    print("Incorrect. Time limit surpassed. (%s seconds)" % (round(endingtime,2)))
                    time.sleep(1)
                    return 0
                elif anw == number1*number2:
                    print("Correct!")
                    time.sleep(1)
                    return 1
                CurrentAttempts += 1
                print("Incorrect.", end=' ')
            except ValueError:
                endingtime = time.time() - startingtime
                if endingtime >= MultiplicationQuiz.TIMEPERQ:
                    print("Incorrect. Time limit surpassed. (%s seconds)" % (round(endingtime,2)))
                    time.sleep(1)
                    return 0
                else:
                    print("Incorrect. Invalid Input. Please enter an integer value.")
                    CurrentAttempts += 1
        print("All attempts used.")
        time.sleep(1)
        return 0

    def start_quiz(self):
        """Main loop for the quiz."""
        for i in range(MultiplicationQuiz.NQUESTIONS):
            n1 = random.randint(0,9)
            n2 = random.randint(0,9)
            StartTime = time.time()
            try:
                answer = int(input('%s x %s = ' % (n1, n2)))
                timetaken = time.time() - StartTime
                if timetaken >= MultiplicationQuiz.TIMEPERQ:
                    print("Incorrect. Time limit surpassed. (%s seconds)" % (round(timetaken,2)))
                    continue
                if answer == n1*n2:
                    print("Correct!")
                    time.sleep(1)
                    self.n_correct += 1
                else:
                    print("Incorrect." , end = ' ')
                    self.n_correct += self.incorrect(n1, n2, StartTime)
            except ValueError:
                print("Incorrect. Invalid Input. Please enter an integer value.")
                self.n_correct += incorrect(n1, n2, ntries, StartTime, timeperq)

    def display_result(self):
        """Displays the result of the quiz."""
        input("You got %s out of %s correct.↲" % (self.n_correct, MultiplicationQuiz.NQUESTIONS))

if __name__ == "__main__":
    multiplication_quiz = MultiplicationQuiz()
    multiplication_quiz.main()