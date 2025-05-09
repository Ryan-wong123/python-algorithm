class Stack:
    def __init__(self):
        self.top = -1
        self.data = []

    def push(self, value):
        self.data.append(value)
        self.top += 1

    def pop(self):
        value = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return value

    def print(self):
        print(self.top)
        print(self.data)

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.data[self.top]

    def printStack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack contents:")
            for i in range(self.top, -1, -1):
                print(self.data[i])

    def invert(self):
        temp_data = []
        while not self.is_empty():
            temp_data.append(self.pop())

        # Replace internal data directly
        self.data = temp_data
        self.top = len(self.data) - 1

aStack = Stack()
aStack.print()
aStack.push(10)
aStack.print()
aStack.push(100)
aStack.print()
aStack.pop()
aStack.print()
aStack.push(99)
aStack.print()
aStack.invert()
aStack.print()
