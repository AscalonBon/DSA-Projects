num1 = float(input('First number: '))
num2 = float(input('Second number: '))

print('1. Addition / 2. Subtraction / 3. Multiplication / 4. Division')
op = input('Operation: ')

# format for solving
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):    
    return num1 / num2

# solving conditions
if op  == '1':
    print('The answer is:', (add(num1, num2)))

elif op  == '2':
    print('The answer is:', (sub(num1, num2))) 

elif op  == '3':
    print('The answer is:', (mult(num1, num2))) 

elif op  == '4':
    print('The answer is:', (div(num1, num2))) \

else:
    print('Please pick a number')

next_calc = input('Proceed with new calculation?')
