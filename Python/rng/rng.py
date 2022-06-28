from random import sample

class RNG:
    def __init__(self):
        self.n_numbers = ""
        self.upper_range = 0
        self.lower_range = 0

    def obtain_value(self, message):
        while True:
            value = input(message)
            if value.isnumeric():
                return int(value)
            else:
                print("Invalid input. Enter an integer value.")

    def obtain_n_numbers(self):
        while True:
            self.n_numbers = self.obtain_value("Enter the number of values to generate: ")
            if self.n_numbers <= 0:
                print("Invalid input. Enter a value greater than 0.")
                continue
            return

    def obtain_upper_range(self):
        while True:
            self.upper_range = self.obtain_value("Enter the upper range of the values: ")
            if self.upper_range <= self.lower_range:
                print("Invalid input. Enter a value larger than the lower range.")
                continue
            elif self.upper_range - self.lower_range < self.n_numbers-1:
                print("Invalid input. The range is too small.")
                continue
            break

    def obtain_range(self):
        self.lower_range = self.obtain_value("Enter the lower range of the values: ")
        self.obtain_upper_range()

    def generate_values(self):
        values = sample(range(self.lower_range,self.upper_range+1),self.n_numbers)
        values.sort()
        input(values)

    def generate_numbers(self):
        self.obtain_n_numbers()
        self.obtain_range()
        self.generate_values()

if __name__ == "__main__":
    rng = RNG()
    rng.generate_numbers()
