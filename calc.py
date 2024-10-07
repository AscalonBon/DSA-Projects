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
                    print('1. Addition / 2. Subtraction / 3. Multiplication / 4. Division: ')
                    self.op = int(input('Choose an operation: '))
                    if self.op in [1, 2, 3, 4]:
                        break
                    else:
                        print('Please choose a number from 1 to 4.')
                except ValueError:
                    print('Please choose a number from 1 to 4.')

            self.x = float(input('First Number: '))
            self.y = float(input('Second Number: '))

            self.operation()

            if not self.next_calc():
                print('Goodbye!')
                break

# Create an instance of Calculator and run it
calc = Calculator()
calc.run()
