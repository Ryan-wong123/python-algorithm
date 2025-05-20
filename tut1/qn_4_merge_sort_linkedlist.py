from singlylinkedlist import SinglyListNode, SinglyLinkedList


# Prepare the lists
list1 = SinglyLinkedList()
for val in reversed([3, 6, 6, 10, 45, 45, 50]):
    list1.insertAtHead(SinglyListNode(val))

list2 = SinglyLinkedList()
for val in reversed([2, 3, 55, 60]):
    list2.insertAtHead(SinglyListNode(val))

# Merge function (reuse this from before)
def merge_sorted_lists(head1, head2):
    dummy = SinglyListNode(0)
    tail = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1
    else:
        tail.next = head2

    return dummy.next

# Merge them
merged_head = merge_sorted_lists(list1.head, list2.head)

# Print the result
print("Merged List:")
while merged_head:
    print(merged_head.data, end=" ")
    merged_head = merged_head.next
