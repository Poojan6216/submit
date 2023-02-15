import json

class Parser:
    def __init__(self, expression):
        self.expression = expression
        self.index = 0

    def parse(self):
        self.index = 0
        return self.parse_E()

    def parse_E(self):
        t = self.parse_T()
        while self.index < len(self.expression) and self.expression[self.index] == '+':
            self.index += 1
            t += self.parse_T()
        return t

    def parse_T(self):
        f = self.parse_F()
        while self.index < len(self.expression) and self.expression[self.index] == '*':
            self.index += 1
            f *= self.parse_F()
        return f

    def parse_F(self):
        if self.expression[self.index].isdigit():
            value = 0
            while self.index < len(self.expression) and self.expression[self.index].isdigit():
                value = value * 10 + int(self.expression[self.index])
                self.index += 1
            return value
        elif self.expression[self.index] == '(':
            self.index += 1
            value = self.parse_E()
            if self.expression[self.index] != ')':
                raise Exception("Expected )")
            self.index += 1
            return value
        else:
            raise Exception("Unexpected character: " + self.expression[self.index])

expression = input("Enter an expression: ")

parser = Parser(expression)
result = parser.parse()

print(json.dumps({"result": result}))
