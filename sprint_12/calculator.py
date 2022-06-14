# номер успешной посылки ID 68957245
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('empty_stack')


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
        else:
            try:
                stack.push(digitizer(element))
            except IndexError:
                raise IndexError('digitization_error')
    return stack.pop()


if __name__ == '__main__':
    print(calculator(input().split(' ')))
