precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '%': 2,
    '**': 3
}

def infix_to_prefix(infix):
    """Converts infix to prefix."""
    operators = []
    prefix = ''
    infix = infix.replace(",", "")  # Treat comma as empty space
    
    infix = infix[::-1]
    
    for char in infix:
        if char.isalnum() or char.isspace():
            prefix = char + prefix
        elif char == ')':
            operators.append(char)
        elif char == '(':
            while operators[-1] != ')':
                prefix = operators.pop() + prefix
            operators.pop()
        else:
            while operators and operators[-1] != ')' and precedence.get(operators[-1], 0) > precedence.get(char, 0):
                prefix = operators.pop() + prefix
            operators.append(char)
    
    while operators:
        prefix = operators.pop() + prefix
    
    return prefix

def infix_to_postfix(infix):
    """Converts infix to postfix."""
    operators = []
    postfix = ''
    infix = infix.replace(",", "")  # Treat comma as empty space
    
    for char in infix:
        if char.isalnum() or char.isspace():
            postfix += char
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators[-1] != '(':
                postfix += operators.pop()
            operators.pop()
        else:
            while operators and operators[-1] != '(' and precedence.get(operators[-1], 0) >= precedence.get(char, 0):
                postfix += operators.pop()
            operators.append(char)
    
    while operators:
        postfix += operators.pop()
    
    return postfix

def prefix_to_infix(prefix):
    """Converts prefix to infix."""
    stack = []
    prefix = prefix.replace(",", "")  # Treat comma as empty space
    
    for char in prefix[::-1]:
        if char.isalnum() or char.isspace():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(f"({operand1}{char}{operand2})")
    
    return stack[0]

def postfix_to_infix(postfix):
    """Converts postfix to infix."""
    stack = []
    postfix = postfix.replace(",", "")  # Treat comma as empty space
    
    for char in postfix:
        if char.isalnum() or char.isspace():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(f"({operand1}{char}{operand2})")
    
    return stack[0]

def postfix_to_prefix(postfix):
    """Converts postfix to prefix."""
    return infix_to_prefix(postfix_to_infix(postfix))

def prefix_to_postfix(prefix):
    """Converts prefix to postfix."""
    return infix_to_postfix(prefix_to_infix(prefix))

def check_brackets(infix):
    """Checks for bracket mismatch."""
    stack = []
    infix = infix.replace(",", "")  # Treat comma as empty space
    
    for char in infix:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    
    return not stack

def print_table(expression, infix, prefix, postfix):
    """Prints the results in a table."""
    print("\nExpression Conversion Results:")
    print("---------------------------------")
    print("| Expression       | Infix       | Prefix      | Postfix     |")
    print("---------------------------------")
    print(f"| {expression} | {infix} | {prefix} | {postfix} |")
    print("---------------------------------")

def main():
    while True:
        print("\nExpression Converter")
        print("---------------------")
        
        expression = input("Enter an expression(s): ")
        expressions = [expr.strip() for expr in expression.split(",")]
        
        combined_expr = "".join(expressions)
        
        if not check_brackets(combined_expr):
            print(f"Error: Bracket mismatch in expression. Please check your expression.")
            continue
        
        infix_expr = combined_expr
        prefix_expr = infix_to_prefix(combined_expr)
        postfix_expr = infix_to_postfix(combined_expr)
        
        print_table(expression, infix_expr, prefix_expr, postfix_expr)
        
        while True:
            cont = input("\nDo you want to continue? (y/n): ").lower()
            if cont == 'y':
                break
            elif cont == 'n':
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()