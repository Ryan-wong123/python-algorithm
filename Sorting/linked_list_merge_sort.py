from Sorting.Single_Linked_List import LinkedList

#sort linked list in ascending order
def MergeSort(linkedlist):
    if(linkedlist.Size() == 1):
        return linkedlist
    elif linkedlist.head is None:
        return linkedlist
        
    leftHalf, rightHalf = Split(linkedlist)

    left = MergeSort(leftHalf)
    right = MergeSort(rightHalf)

    return Merge(left,right)

def Split(linkedList):
    #if the linked list is empty
    if(linkedList is None or linkedList.head is None):
        leftHalf = linkedList
        righthalf = None

        return leftHalf,righthalf
    else:
        size = linkedList.Size()
        mid = size//2
        
        #get the mid point node
        midNode = linkedList.NodeAtIndex(mid - 1)

        #assign the left half of the initial linked list 
        leftHalf = linkedList

        #create a new linked list and assign the right half of the initial linked list to the new linked list
        righthalf = LinkedList()
        righthalf.head = midNode.nextNode

        #break off the connection of the initial linkedlist by setting the mid point node as the tail of the new left sublist
        midNode.nextNode = None

        return leftHalf,righthalf
    
#merge 2 linked list and sort the data by the nodes
def Merge(left,right):
    #create new linked list that contains nodes from merging left and right
    merged = LinkedList()

    #add a fake head that is discarded later
    merged.Add(0)

    #set current as the head of the linked list
    current = merged.head

    #obtain head nodes for left and right linked list
    leftHead = left.head
    rightHead = right.head

    #iterate over left and right until we reach the tail node
    while leftHead or rightHead:
        #if the head none of left is none, means we have passed the tail of the left list
        #add the nodes from the right to the merged linked list
        if leftHead is None:
            current.nextNode = rightHead
            #call next on right to set loop as false
            rightHead = rightHead.nextNode
        #if the head none of right is none, means we have passed the tail of the right list
        #add the tail node from the left to the merged linked list
        elif rightHead is None:
            current.nextNode = leftHead
            #call next on left to set loop condition as false
            leftHead = leftHead.nextNode
        else:
            #not at either tail node 
            #obtain data from body nodes to compare and perform sorting
            leftData = leftHead.data
            rightData = rightHead.data
            
            #if data on the left is less than the data on the right, set current to left Node 
            if(leftData < rightData):
                current.nextNode = leftHead
                #move left head to next node
                leftHead = leftHead.nextNode
            else:
                current.nextNode = rightHead
                #move right head to next node
                rightHead = rightHead.nextNode
    
        #move current to next node
        current = current.nextNode
    #discard fake head and set first merge node as head
    head = merged.head.nextNode
    merged.head = head

    return merged

unsortedList = LinkedList()
unsortedList.Add(5)
unsortedList.Add(45)
unsortedList.Add(75)
unsortedList.Add(32)
unsortedList.Add(89)

sortedLinkedList = MergeSort(unsortedList)
print(sortedLinkedList)
