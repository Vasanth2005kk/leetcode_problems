from typing import Optional
from  linkedlistfunc import createNode , LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        SortValue = []
        count = 1
        temp = head
        while temp:
            if count >= left and count <= right:
                SortValue.append(temp.val)
            count +=1
            temp = temp.next

        Values = SortValue[::-1]

        valueIndex = 0
        count = 1
        temp = head
        while temp:
            if count >= left and count <= right:
                temp.val = Values[valueIndex]
                valueIndex+=1
            count +=1
            temp = temp.next

        return head
        
                

head = [1,2,3,4,5]
left = 2
right = 4

head =  createNode(head)

obj = Solution().reverseBetween(head,left,right)
LinkedListPrint(obj)