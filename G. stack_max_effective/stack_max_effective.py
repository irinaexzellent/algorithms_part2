class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = None
        self.items_max = []
    
    def push(self, item):
        self.items.append(item)
        if len(self.items_max) == 0:
            self.max = item
            self.items_max.append(self.max)
        elif item > self.max:
            self.max = item
            self.items_max.append(self.max)
        else:
            self.items_max.append(self.max)


    def pop(self):
        if len(self.items) == 0:
            print('error')
        else:
            removed = self.items.pop()
            removed_max = self.items_max.pop()
            if len(self.items) == 0:
                self.max = None
            elif len(self.items) == 1:
                 self.max = self.items[0]
            elif removed == self.max:
                self.max = self.items_max[-1]
                #self.max = self.items[0]
                #for value in self.items:
                #    if value > self.max:
                #        self.max = value
            return removed

    def get_max(self):
        return self.max
    
    def isEmpty(self):
        return not self

    
if __name__ == '__main__':
    stack = StackMaxEffective()
    
    count = int(input())
    commands = []
    while count != 0:
        commands.append(str(input()))
        count -= 1
    #print(commands)
    
    index = 0
    while index!= len(commands):
        if commands[index] == 'get_max':
            print(stack.get_max())
        elif commands[index].startswith('push'):
            string = commands[index].split(' ')
            digit = int(string[1])
            stack.push(digit)
        elif commands[index] == 'pop':
            stack.pop()
        index += 1