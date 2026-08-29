from typing import Optional
from linkedlistfunc import createNode , LinkedListPrint


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val =  val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0 or not head.next:
            return head 

        length = 1
        current = head
        
        while(current.next):
            length +=1
            current =  current.next

        final_k = k % length
        if final_k == 0:
            return head

        current.next =  head

        breakindex = length - final_k -1
        print(f"ll-length = {length}  brack point :{breakindex}, k Value : {final_k}")

        tail = head
        for i in range(breakindex):
            tail = tail.next

        newhead =  tail.next
        tail.next = None

        return newhead


head = [1,2]
k = 2


head = createNode(head)

obj =  Solution().rotateRight(head,k)
LinkedListPrint(obj)