# номер успешной посылки ID 68955013
class Deque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 1
        self.tail = 0
        self.size = 0

    def push_front(self, value):
        if self.size == self.max_size:
            raise OverflowError
        self.head = (self.head - 1) % self.max_size
        self.items[self.head] = value
        self.size += 1

    def push_back(self, value):
        if self.size == self.max_size:
            raise OverflowError
        self.tail = (self.tail + 1) % self.max_size
        self.items[self.tail] = value
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise OverflowError
        value = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    def pop_back(self):
        if self.size == 0:
            raise OverflowError
        value = self.items[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return value


if __name__ == '__main__':
    command_count = int(input())
    deque = Deque(max_size=int(input()))
    for _ in range(command_count):
        try:
            command, *params = input().split(' ')
            result = getattr(deque, command)(*params)
            if 'pop' in command:
                print(result)
        except OverflowError:
            print('error')
