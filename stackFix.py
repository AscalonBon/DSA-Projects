class PostfixStackImplementation:
    def __init__(self):
        self.operator_list = ['+', '-', '*', '/']
        self.operand_list = []
        self.result = []
        self.stack = []

    def precedence(self, operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        return 0

    def stackPostfix(self, expression):
        for char in expression:
            if char.isalpha() or char.isnumeric():
                self.result.append(char)
            elif char in self.operator_list:
                while (self.stack and self.precedence(self.stack[-1]) >= self.precedence(char)):
                    self.result.append(self.stack.pop())
                self.stack.append(char)

        while self.stack:
            self.result.append(self.stack.pop())

        return ''.join(self.result)

    def main(self):
        initial = input("Input expression: ")
        postfix = self.stackPostfix(initial)
        print(f"Postfix expression: {postfix}")


if __name__ == "__main__":
    postfix_converter = PostfixStackImplementation()
    postfix_converter.main()
