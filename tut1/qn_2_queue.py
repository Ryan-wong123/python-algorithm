class Queue:
    def __init__(self):
        self.rear = -1
        self.data = []

    def enqueue(self, value):
        self.data.append(value)
        self.rear += 1

    def dequeue(self):
        value = self.data[0]
        del self.data[0]
        self.rear -= 1
        return value

    def print(self):
        print(self.rear)
        print(self.data)
    
    def is_empty(self):
        return self.rear == -1

    def peek(self):
        if self.is_empty():
            return None
        return self.data[0]
    
    def print_Queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue contents:")
            for i in range(self.rear + 1):
                print(self.data[i], end=" ")
            print()

aQueue = Queue()
aQueue.print()
print(aQueue.is_empty())
aQueue.enqueue(8)
aQueue.print()
aQueue.enqueue(-5)
aQueue.print()
aQueue.dequeue()
aQueue.print()
aQueue.enqueue(2)
aQueue.print()
print(aQueue.peek())
aQueue.dequeue()
aQueue.print()
print(aQueue.is_empty())
print(aQueue.peek())
aQueue.dequeue()
aQueue.print()