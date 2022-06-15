# номер успешной посылки ID 68967320
class Deque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 1
        self.tail = 0
        self.size = 0

    def push_front(self, params):
        if self.size == self.max_size:
            raise RuntimeError('error')
        self.head = (self.head - 1) % self.max_size
        self.items[self.head] = params
        self.size += 1

    def push_back(self, params):
        if self.size == self.max_size:
            raise RuntimeError('error')
        self.tail = (self.tail + 1) % self.max_size
        self.items[self.tail] = params
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise RuntimeError('error')
        params = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return params

    def pop_back(self):
        if self.size == 0:
            raise RuntimeError('error')
        params = self.items[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return params


if __name__ == '__main__':
    command_count = int(input())
    deque = Deque(max_size=int(input()))
    for _ in range(command_count):
        try:
            command, *params = input().split(' ')
            result = getattr(deque, command)(*params)
            if '' in command and result is not None:
                print(result)
        except RuntimeError:
            print('error')
        except AttributeError:
            raise ValueError(
                ('command not found: {command}').format(command=command)
            )
