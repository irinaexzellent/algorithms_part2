class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class MyQueueSized:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0 

    def isEmpty(self):
        return self.front is None

    def size_q(self):
        y = int(self.size)
        return y

    def put(self, item):
        temp = Node(item)
        if (self.rear is None and self.front is None):
            self.front = self.rear = temp
            self.size += 1
            return
        self.rear.next_item = temp
        self.rear = temp
        self.size += 1
        
    def get(self):
        if self.isEmpty():
            return 'error'
        temp = self.front
        #self.front = temp.next_item

        if self.front == self.rear:
            self.front = self.rear = None
            self.size -= 1
            
        else:
           temp = self.front
           self.front = temp.next_item
           self.size -= 1
        if temp != None:
            return temp.value


if __name__ == '__main__':
    count = int(input())
    
    stack = MyQueueSized()
    commands = []

    while count != 0:
        commands.append(str(input()))
        count -= 1
    index = 0
    while index!= len(commands):
        if commands[index].startswith('put'):
            string = commands[index].split(' ')
            digit = int(string[1])
            stack.put(digit)
        elif commands[index] == 'size':
            print(stack.size_q())
        elif commands[index] == 'get':
            print(stack.get())
        index += 1