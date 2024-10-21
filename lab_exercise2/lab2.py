class Calculator:
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
                    print('1. Addition / 2. Subtraction / 3. Multiplication / 4. Division / 5. Factorial: ')
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


class AreaSolver:
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
            print('1. Square / 2. Rectangle / 3. Triangle / 4. Circle')
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

class FunctionOverloader:
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

def main():
    overloader = FunctionOverloader()
    overloader.linechar()  
    overloader.linechar('@')  
    overloader.linechar(10)  
    overloader.linechar('#', 15)  

    input("Press Enter to exit...")  

def main():
    while True:
        print('Welcome to the Extended Program!')
        print('1. Calculator / 2. Area Solver / 3. LineChar Overloader')
        try:
            choice = int(input('Choose a program: '))
            if choice == 1:
                calc = Calculator()
                calc.run()
            elif choice == 2:
                area_solver = AreaSolver()
                area_solver.run()
            elif choice == 3:
                main()  # Call the linechar overloading function
            else:
                print('Please choose a valid option (1, 2, or 3).')
        except ValueError:
            print('Please enter a valid number (1, 2, or 3).')

        proceed = input('Do you want to continue using the program? (Y/N): ').upper()
        if proceed != 'Y':
            print('Goodbye!')
            break


# Start the extended main program
main()
