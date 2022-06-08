class MyQueueSized:
    def __init__(self, n):
        self.queue = [None]*n
        self.max_size = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def size_q(self):
        y =int(self.size)
        return y

    def peek(self):
        if self.is_empty():
            return 'None'
        return self.queue[self.head]

    def push(self, x):
        if self.size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print ('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return x


if __name__ == '__main__':
    count = int(input())
    size_queue = int(input())

    stack = MyQueueSized(size_queue)
    commands = []

    while count != 0:
        commands.append(str(input()))
        count -= 1

    index = 0
    while index!= len(commands):
        if commands[index] == 'peek':
            print(stack.peek())
        elif commands[index] == 'size':
            print(stack.size_q())
        elif commands[index].startswith('push'):
            string = commands[index].split(' ')
            digit = int(string[1])
            stack.push(digit)
        elif commands[index] == 'pop':
            print(stack.pop())
        index += 1