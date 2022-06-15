# номер успешной посылки ID 68972231
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('empty stack')


OPERATORS = {
    '+': lambda left, right: left + right,
    '-': lambda left, right: left - right,
    '*': lambda left, right: left * right,
    '/': lambda left, right: left // right,
}


def calculator(expression, stack=None, operators=OPERATORS, digitizer=int):
    stack = Stack() if stack is None else stack
    for element in expression:
        if element in operators:
            right, left = stack.pop(), stack.pop()
            stack.push(operators[element](left, right))
            continue
        try:
            stack.push(digitizer(element))
        except ValueError:
            raise ValueError(f'incorrect operator: {element}')
    return stack.pop()


if __name__ == '__main__':
    print(calculator(input().split(' ')))
