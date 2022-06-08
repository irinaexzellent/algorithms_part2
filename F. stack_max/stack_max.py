class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("error")
        else:
            removed = self.items.pop()
            return removed

    def get_max(self):
        if len(self.items) == 0:
            self.max = None
        else:
            self.max = self.items[0]
            for value in self.items:
                if value > self.max:
                    self.max = value
        return self.max

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    stack = StackMax()

    count = int(input())
    commands = []
    while count != 0:
        commands.append(str(input()))
        count -= 1

    index = 0
    while index != len(commands):
        if commands[index] == 'get_max':
            print(stack.get_max())
        elif commands[index].startswith('push'):
            string = commands[index].split(' ')
            digit = int(string[1])
            stack.push(digit)
        elif commands[index] == 'pop':
            stack.pop()
        index += 1
