class ModeChooser:
    def __init__(self):
        pass  # No need for a state attribute here
class ModeChooser:
    def __init__(self):
        pass

    def run(self):
        while True:
            print('1. Number Array / 2. Decimal to Binary / 3. Number Identifier / 4. Palindrome Checker')
            try:
                choice = int(input('Choose a mode: '))
                if 1 <= choice <= 4:
                    if choice == 1:
                        number_array = NumberArray()
                        number_array.get_numbers()
                        number_array.ascend()
                    elif choice == 2:
                        decimal_to_binary = DecimaltoBinary()
                        while True:
                            try:
                                decimal_num = int(input("Enter a positive decimal number: "))
                                decimal_to_binary.converter(decimal_num)
                                decimal_to_binary.display_binary()
                                break
                            except ValueError as e:
                                print(e)
                    elif choice == 3:
                        identifier = Identifier()
                        identifier.get_numbers()
                        identifier.value_finder()
                    elif choice == 4:
                        palindrome_checker = PalindromeChecker()
                        while True:
                            word = input("Enter a word: ")
                            if palindrome_checker.checker(word):
                                print(f"{word} is a palindrome.")
                            else:
                                print(f"{word} is not a palindrome.")
                            if input("Check another word? (y/n): ").lower() != 'y':
                                break

                    # Check for "y" or "n" only
                    while True:
                        another_mode = input("Run another mode? (y/n): ").lower()
                        if another_mode == 'y':
                            break
                        elif another_mode == 'n':
                            return  # Exit the program
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")

                else:
                    print('Invalid choice. Please enter a number between 1 and 4.')
            except ValueError:
                print('Invalid input. Please enter a number.')

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
            remainder = decimal_num % 2
            self.binary_array.append(remainder)
            decimal_num //= 2

        self.binary_array.reverse()  # binary correction

    def display_binary(self):
        print('Binary representation:', ''.join(str(x) for x in self.binary_array))

class Identifier:
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

    def value_finder(self):
        if len(self.numbers) < 2:
            raise ValueError('2 numbers are required!')

        highest1 = highest2 = self.numbers[0]
        lowest1 = lowest2 = self.numbers[0]

        for i in range(1, len(self.numbers)):
            num = self.numbers[i]
            if num > highest1:
                highest2 = highest1
                highest1 = num
            elif num > highest2:
                highest2 = num
            if num < lowest1:
                lowest2 = lowest1
                lowest1 = num
            elif num < lowest2:
                lowest2 = num

        print("1st highest:", highest1)
        print("2nd highest:", highest2)
        print("1st lowest:", lowest1)
        print("2nd lowest:", lowest2)

class PalindromeChecker:
    def __init__(self):
        pass

    def checker(self, word):
        word = word.lower()
        return word == word[::-1]


# Start the program
mode_chooser = ModeChooser()
mode_chooser.run()