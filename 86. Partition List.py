from linkedlistfunc import LinkedListPrint, createNode
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessnums = []
        graternums =[]

        curr = head
        while curr:
            if curr.val < x:
                lessnums.append(curr.val)
            else:
                graternums.append(curr.val)
            curr =  curr.next

        orderlist = lessnums+graternums

        temp = head
        index  = 0
        while temp:
            temp.val = orderlist[index]
            index+=1
            temp = temp.next

        return head

head = [1,4,3,2,5,2]
x = 3

head = createNode(head)
obj = Solution().partition(head,x)
LinkedListPrint(obj)