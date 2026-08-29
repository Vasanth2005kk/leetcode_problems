from linkedlistfunc import createNode , LinkedListPrint
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current =  head
        while current:
            length +=1
            current = current.next

        if length <= 1:
            return head

        mid = (length//2)-1

        current = head
        count = 0
        new_head = None
        while current:
            if count >= mid:
                new_head = current.next
                return new_head
            count +=1
            current = current.next


head = [1,2,3,4,5] 
head =  createNode(head)
obj = Solution().middleNode(head)

LinkedListPrint(obj)