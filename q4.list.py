class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

def merge_two_lists(list1, list2):
    dummy = ListNode() 
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    return dummy.next


list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)


list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)


merged_list_head = merge_two_lists(list1, list2)

print("Merged sorted list:")
print_linked_list(merged_list_head)



