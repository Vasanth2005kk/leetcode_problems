from linkedlistfunc import createNode , LinkedListPrint
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = []
        even = []
        count = 0
        current = head

        while current:
            count +=1
            if count % 2 == 1:
                odd.append(current.val)
            else:
                even.append(current.val)

            current = current.next
        arr = odd+even
        
        current = head
        for i in arr:
            current.val = i
            current = current.next

        return head

head = [1,2,3,4,5]
head = createNode(head)

obj = Solution().oddEvenList(head)
print(obj)