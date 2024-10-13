class NumberArray:
    def __init__(self):
        self.numbers = []
    
    def get_numbers(self):
        for i in range(10):
            while True:
                try:
                    number = float(input(f"Enter number {i+1}: "))
                    self.numbers.append(number)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

    def ascend(self):
        self.numbers.sort()
        print('The values in ascending order: ', self.numbers)
    
class DecimaltoBinary:
    def __init__(self):
        self.binary_array = []
    
    def converter(self, decimal_num):
        if decimal_num < 0:
            raise ValueError('Input must be positive numbers!')

        while decimal_num > 0:
            remainder = decimal_num %2
            self.binary_array.append(remainder)
            decimal_num //= 2
        
        self.binary_array.reverse()  # Reverse the array to get the correct binary representation

    def display_binary(self):
        print('Binary representation:', ''.join(str(x) for x in self.binary_array))

class Indentifier:
    def __init__(self):
        self.numbers = []

    def get_numbers(self):
        for i in range(10):
            while True:
                try:
                    number = float(input(f"Enter number {i+1}: "))
                    self.numbers.append(number)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
    



