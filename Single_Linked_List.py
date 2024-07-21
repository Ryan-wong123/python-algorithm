class Node:

    data = None
    nextNode = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "Node data %s" % self.data
    
class LinkedList:
    head = None

    def __init__(self):
        self.head = None
    
    #check if list is empty 
    def IsEmpty(self):
        return self.head == None
    
    #return the number of nodes in the list uses O(n) time complexity
    def Size(self):
        current  = self.head
        count = 0
        #while current node is not the tail
        while current != None:
            count += 1
            current = current.nextNode
        return count
    
    #adding new node at the head of the list, O(1) time complexity
    def Add(self,data):
        newNode = Node(data)
        #set the next node of the new head from the current head reference to prevent any breakage of references in the list
        newNode.nextNode = self.head
        #set the new node as the head
        self.head = newNode

    #search for the first node in the linked list that contains data that matches the key
    def Search(self,key):
        current = self.head

        while current !=  None:
            if current.data == key:
                return current
            else:
                current = current.nextNode
        return None
    
    def Insert(self,data,index):
        #if the index is the first means add the node to the linked list as the new head
        if(index == 0):
            self.Add(data)
        
        #if the index is not the head
        if(index > 0):
            newNode = Node(data)
            
            position = index
            currentNode = self.head

            while position > 1:
                currentNode = currentNode.nextNode
                position -= 1

            previousNode = currentNode
            nextNode = currentNode.nextNode

            previousNode.nextNode = newNode
            newNode.nextNode = nextNode
            
    #remove the node that contains the data that matches the key with O(n) time complexity
    def Remove(self, key):
        currentNode = self.head
        previousNode = None
        found = False

        while(currentNode != None and  not found):
            #if the current node that holds the data of the key is the head
            if currentNode.data == key and currentNode == self.head:
                found = True
                self.head = currentNode.nextNode
            #if the current node that holds the data of the key is the body or tail
            elif currentNode.data == key:
                found = True
                previousNode.nextNode = currentNode.nextNode
            #if the current node does not contain data of the key
            else:
                previousNode = currentNode
                currentNode = currentNode.nextNode

        return currentNode

    #return a string representation of the linked list, O(n) time complexity
    def __repr__(self):

        nodes = []
        current = self.head
        #while current node is not the tail
        while current != None:
            #if current node is head
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            #if current node is tail
            elif current.next is None:
                nodes.append("[Tail: %s]" % current.data)
            #if current node is the body 
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)
