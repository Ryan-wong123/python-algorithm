class SinglyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.data is value:
                return temp
            temp = temp.next
        print( 'Search Error: Value not found' )
    def insertAtHead(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def delete(self, value):
        prev = None
        temp = self.head
        while temp is not None:
            if temp.data is not value:
                prev = temp
                temp = temp.next
            else:
                if temp == self.head:
                    self.deleteAtHead()
                else:
                    prev.next = temp.next
                    del temp
                return
        print( 'Value ', value, ' cannot be found' )

    def deleteAtHead(self):
        """Delete the first node in the list."""
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        self.head = self.head.next

    def printList(self):
        print('Current list content:')
        temp = self.head
        while temp is not None:
            print( '[',temp.data,']' )
            temp = temp.next
        print()


aList = SinglyLinkedList()
aNode = SinglyListNode(15)
aList.insertAtHead(aNode)
aNode2 = SinglyListNode(30)
aList.insertAtHead(aNode2)
aNode3 = SinglyListNode(40)
aList.insertAtHead(aNode3)
aList.printList()

aList.delete(30)
aList.printList()
aList.delete(3)
