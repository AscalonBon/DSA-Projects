next = 'y'
while next:
    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))

    print('1. Addition / 2. Subtraction / 3. Multiplication / 4. Division / 5. Reset input')
    op = int(input('Operation: '))

    #format for solving
    def add(num1, num2):
        return num1 + num2

    def sub(num1, num2):
        return num1 - num2

    def mult(num1, num2):
        return num1 * num2

    def div(num1, num2):    
        return num1 / num2

    #solving conditions
    if op  == 1:
        print('The answer is:', (add(num1, num2)))

    elif op  == 2:
        print('The answer is:', (sub(num1, num2))) 

    elif op  == 3:
        print('The answer is:', (mult(num1, num2))) 

    elif op  == 4:
        if num2 == 0:
            print('This cannot be')
        else:
            print('The answer is:', (div(num1, num2))) 
    
    elif op == 5:
        print('Input new numbers')
        continue

    else:
        print('Invalid operation. Please select a valid operation (1-5)')
    
    next = input('Next calculation? (Y/N): ').lower()
    if next == 'n':
        break
    
