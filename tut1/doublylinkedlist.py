class DoublyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtHead(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def delete(self, value):
        temp = self.head
        while temp is not None:
            if temp.data is not value:
                temp = temp.next
            else:
                if temp is self.head:
                    self.head = self.head.next
                elif temp is self.tail:
                    self.tail = self.tail.prev
                else:
                    prev = temp.prev
                    succ = temp.next
                    prev.next = succ
                    succ.prev = prev
                del temp
                return
        print( 'Delete: Value not found' )

    def printList(self):
        print('Current list content:')
        temp = self.head
        while temp is not None:
            print( '[',temp.data,']' )
            temp = temp.next
        print()

aList = DoublyLinkedList()
aNode = DoublyListNode(15)
aList.insertAtHead(aNode)
aNode2 = DoublyListNode(30)
aList.insertAtHead(aNode2)
aNode3 = DoublyListNode(40)
aList.insertAtHead(aNode3)
aList.printList()

aList.delete(30)
aList.printList()
aList.delete(3)
