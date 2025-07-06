# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, 
# except the number 0 itself.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next

# Helper functions for testing
def list_to_linkedlist(lst):
    dummy = ListNode()
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage:
l1 = list_to_linkedlist([2,4,3])  # represents 342
l2 = list_to_linkedlist([5,6,4])  # represents 465
result = add_two_numbers(l1, l2)  # should represent 807
print(linkedlist_to_list(result))  # Output: [7, 0, 8]