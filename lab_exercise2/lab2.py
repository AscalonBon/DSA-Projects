class Calculator: #problem 1, 3 and 4 
    def __init__(self):
        self.x = 0
        self.y = 0
        self.op = 0
        self.proceed = 'Y'

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return 'Cannot divide by zero!'
        return x / y

    def factorial(self, n):
        # Calculate factorial of n
        if n == 0 or n == 1:
            return 1
        else:
            fact = 1
            for i in range(2, n+1):
                fact *= i
            return fact

    def operation(self):
        if self.op == 1:
            print('The answer is:', self.add(self.x, self.y))

        elif self.op == 2:
            print('The answer is:', self.sub(self.x, self.y))

        elif self.op == 3:
            print('The answer is:', self.multiply(self.x, self.y))

        elif self.op == 4:
            if self.y == 0:
                print('Cannot divide by zero!')
            else:
                print('The answer is:', self.divide(self.x, self.y))

        elif self.op == 5:
            print(f'The factorial of {self.x} is:', self.factorial(self.x))

    def next_calc(self):
        while True:
            self.proceed = input('Do you want to continue? (Y/N): ').upper()
            if self.proceed == 'Y':
                return True
            elif self.proceed == 'N':
                return False
            else:
                print("Please choose Y or N.")

    def run(self):
        while self.proceed.upper() == 'Y':
            while True:
                try:
                    print('Welcome to Calculator!')
                    print('++++++++++++++++++++++++')
                    print('1. Addition / 2. Subtraction / 3. Multiplication / 4. Division / 5. Factorial: ')
                    print('++++++++++++++++++++++++')
                    self.op = int(input('Choose an operation: '))
                    if self.op in [1, 2, 3, 4, 5]:
                        break
                    else:
                        print('Please choose a number from 1 to 5.')
                except ValueError:
                    print('Please choose a number from 1 to 5.')

            while True:
                try:
                    if self.op == 5:
                        self.x = int(input('Enter the number for factorial: '))
                    else:
                        self.x = int(input('First Number: '))
                        if self.op != 5:
                            self.y = int(input('Second Number: '))
                    break
                except ValueError:
                    print('Please enter a valid number.')

            self.operation()

            if not self.next_calc():
                print('Goodbye!')
                break


class AreaSolver: #problem 2
    def __init__(self):
        pass

    def area_square(self, side):
        return side ** 2

    def area_rectangle(self, length, width):
        return length * width

    def area_triangle(self, base, height):
        return 0.5 * base * height

    def area_circle(self, radius):
        return 3.14159 * radius ** 2

    def run(self):
        while True:
            print('Area Calculator')
            print('++++++++++++++++++++++++')
            print('1. Square / 2. Rectangle / 3. Triangle / 4. Circle')
            print('++++++++++++++++++++++++')
            try:
                choice = int(input('Choose a shape: '))
                if choice == 1:
                    side = float(input('Enter the side length of the square: '))
                    print(f'The area of the square is {self.area_square(side)}')
                elif choice == 2:
                    length = float(input('Enter the length of the rectangle: '))
                    width = float(input('Enter the width of the rectangle: '))
                    print(f'The area of the rectangle is {self.area_rectangle(length, width)}')
                elif choice == 3:
                    base = float(input('Enter the base of the triangle: '))
                    height = float(input('Enter the height of the triangle: '))
                    print(f'The area of the triangle is {self.area_triangle(base, height)}')
                elif choice == 4:
                    radius = float(input('Enter the radius of the circle: '))
                    print(f'The area of the circle is {self.area_circle(radius)}')
                else:
                    print('Please choose a valid shape (1-4).')
                    continue
                break
            except ValueError:
                print('Please enter valid numbers.')

class FunctionOverloader: #problem 5
    def __init__(self):
        pass

    def linechar(self, char='-', length=None):
        if char == '-' and length is None:
            print('-' * 10)
        elif length is None:
            print(str(char) * 10)
        elif isinstance(char, int):
            print('-' * char)
        else:
            print(str(char) * length)

def overloader():
    overloader = FunctionOverloader()
    overloader.linechar()  
    overloader.linechar('@')  
    overloader.linechar(10)  
    overloader.linechar('#', 15)  

    input("Press Enter to exit...")  


class Odd_Number_Summation: #problem 6
    def __init__(self):
        self.numbers =[]
        
    def run(self):
        print('Odd Number Summation')
        print('++++++++++++++++++++++++')
        print('Input 10 numbers.')
        print('++++++++++++++++++++++++')
        for _ in range(10):
            try:
                numbers = float(input('Input Number: '))
                if numbers % 2 != 0:
                    self.numbers.append(numbers)

            except ValueError:
                print('Enter valid number.') 
        
        odd_sum = sum(self.numbers)
        print(f'sum of odd numbers is: {odd_sum}')


class Sequential_Summation: #problem 7
    def __init__(self):
        self.four_numbers = []

    def add(self, num_int, number1=None, number2=None, number3=None):
        if num_int == 1:
            return number1 + number2
        elif num_int == 2:
            return number1 + number2 + number3
        elif num_int == 3:
            return sum(self.four_numbers)

    def run(self):
        while True:
            try:
                print('Summation Program')
                print('++++++++++++++++++++++++')
                print('1. Two number input / 2. Three number input / 3. Four number input')
                print('++++++++++++++++++++++++')
                self.num_int = int(input('Enter number input: '))

                if self.num_int == 1:
                    try:
                        self.numbers1 = float(input('Input number 1: '))
                        self.numbers2 = float(input('Input number 2: '))
                        print('The answer is: ', self.add(self.num_int, self.numbers1, self.numbers2))
                        break

                    except ValueError:
                        print('Enter valid number.')

                elif self.num_int == 2:
                    try:
                        self.numbers1 = float(input('Input number 1: '))
                        self.numbers2 = float(input('Input number 2: '))
                        self.numbers3 = float(input('Input number 3: '))
                        print('The answer is: ', self.add(self.num_int, self.numbers1, self.numbers2, self.numbers3))
                        break

                    except ValueError:
                        print('Enter valid number.')

                elif self.num_int == 3:
                    for _ in range(4):
                        try:
                            number = float(input('Input Number: '))
                            self.four_numbers.append(number)
                        except ValueError:
                            print('Enter valid number.')
                    print('The answer is: ', sum(self.four_numbers))
                    break
                else:
                    print('Please choose a valid option (1-3).')

            except ValueError:
                print('Enter valid number.')

class IndexRange:
    def __init__(self):
        self.main_str = ""

    def run(self):
        while True:
            try:
                print('Index Range Analyzer')
                print('++++++++++++++++++++++++')
                self.main_str = input('Enter string value (type "exit" to end program): ')
                if self.main_str.lower() == 'exit':
                    break

                print(f'Length of the string is: {len(self.main_str)}')  
                print('++++++++++++++++++++++++')

            except Exception as e:
                    print(f'An error occurred: {e}')

            while True:
                    try:
                        # index plot points
                        self.substring_val_i = int(input('Enter start index: ')) 
                        if self.substring_val_i < 0:
                            print('Invalid input: Start index cannot be negative.')
                            continue
                        elif self.substring_val_i > len(self.main_str):
                            print(f'Invalid input: Start index exceeds or equals string length {len(self.main_str)}.')
                            continue
                        
                        self.substring_val_e = int(input('Enter end index: '))
                        if self.substring_val_e < 0:
                            print('Invalid input: End index cannot be negative.')
                            continue
                        elif self.substring_val_e > len(self.main_str):
                            print(f'Invalid input: End index exceeds string length {len(self.main_str)}.')
                            continue
                        
                        # Check if start index is less than or equal to end index
                        if self.substring_val_i > self.substring_val_e:
                            print('Invalid input: Start index cannot be greater than end index.')
                            continue
                        
                        break  # Valid input, exit loop

                    except ValueError:
                        print('Please enter a valid number.')

            while True:
                try:
                    print('Main string:', self.main_str)
                    print('++++++++++++++++++++++++')
                    print(f'Substring from index {self.substring_val_i}:', 
                                self.main_str[self.substring_val_i:])
                    print('++++++++++++++++++++++++')
                    print(f'Substring from index {self.substring_val_i} to {self.substring_val_e}:', 
                                self.main_str[self.substring_val_i:self.substring_val_e])
                    print('++++++++++++++++++++++++')

                    break

                except Exception as e:
                            print(f'Error: {e}')        
                        



                
# main loop
def main():
    while True:
        print('Welcome to Lab Exercise #2!')
        print('+++++++++++++++++++++++++++++++++++++++++++++++')
        print('1. Calculator / 2. Area Solver / 3. LineChar Overloader / 4. Odd Number Summarizer')
        print('5. Sequential Summation / 6. Index Range')
        print('+++++++++++++++++++++++++++++++++++++++++++++++')
        try:
            choice = int(input('Choose a program: '))
            if choice == 1:
                calc = Calculator()
                calc.run()
            elif choice == 2:
                area_solver = AreaSolver()
                area_solver.run()
            elif choice == 3:
                overloader()  # Call the linechar overloading function
            elif choice == 4:
                sum_odd = Odd_Number_Summation()
                sum_odd.run()
            elif choice == 5:
                seq_sum = Sequential_Summation()
                seq_sum.run()
            elif choice == 6:
                index_range = IndexRange()
                index_range.run()
            else:
                print('Please choose a valid option.')
        except ValueError:
            print('Please enter a valid number.')
        
        while True:
            proceed = input('Do you want to continue using the program? (Y/N): ').upper()
            if proceed in ['Y', 'N']:
                  break
            else:
                print('Invalid input. Please enter Y or N.')

        if proceed == 'N':
            print('Goodbye!')
            break

# Start the extended main program
main()