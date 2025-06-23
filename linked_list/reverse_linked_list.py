# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None      # Previous node (starts as None)
        curr = head      # Current node starts at the head

        while curr:
            next_node = curr.next  # Temporarily store next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev one step forward
            curr = next_node       # Move curr one step forward

        return prev  # New head of the reversed list

# Helper to create linked list from Python list
def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

# Helper to print linked list
def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(" -> ".join(map(str, vals)))

# Test
head = build_linked_list([1, 2, 3, 4, 5])
print("Original list:")
print_linked_list(head)

sol = Solution()
reversed_head = sol.reverseList(head)

print("Reversed list:")
print_linked_list(reversed_head)

