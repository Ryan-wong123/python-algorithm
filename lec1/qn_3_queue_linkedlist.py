from singlylinkedlist import SinglyListNode, SinglyLinkedList

class LinkedQueue:
    def __init__(self):
        self.list = SinglyLinkedList()      # This is our queue's internal structure
        self.tail = None                    # We keep track of the end of the queue

    def is_empty(self):
        return self.list.head is None


    def enqueue(self, value):
        new_node = SinglyListNode(value)  # Create a new node
        if self.is_empty():               # If queue is empty
            self.list.head = new_node     # Make it the head
            self.tail = new_node          # Also the tail
        else:
            self.tail.next = new_node     # Add new node after tail
            self.tail = new_node          # Update tail to new node


    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        value = self.list.head.data       # Get the value at the front
        self.list.deleteAtHead()          # Remove the front node
        if self.list.head is None:        # If the list is now empty
            self.tail = None              # Clear the tail
        return value                      # Return the removed value

    def peek(self):
        if self.is_empty():
            return None
        return self.list.head.data        # Just look at the head value


    def print_queue(self):
        print("Queue contents:")
        temp = self.list.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()
