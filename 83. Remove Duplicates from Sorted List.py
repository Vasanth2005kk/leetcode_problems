from typing import Optional

# Helper functions for linked list creation and display
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" --> ")
        current = current.next
    print("None")

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

# Test the code
head = [1, 1, 2]
head = create_linked_list(head)
print("Original list:")
print_linked_list(head)

obj = Solution()
head = obj.deleteDuplicates(head)

print("List after removing duplicates:")
print_linked_list(head)
