from typing import Optional
from linkedlistfunc import createNode , LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kGroup = []

        temp =  head
        kValues = []
        while temp:
            if len(kValues) < k:
                kValues.append(temp.val)

                if len(kValues) == k:
                    kGroup.extend(kValues[::-1])
                    kValues = []

            temp =  temp.next
        kGroup.extend(kValues)
        # print("modifyed Values :",kGroup)

        index = 0
        temp = head
        while temp:
            temp.val = kGroup[index]
            index+=1
            temp = temp.next

        return head

head = [1,2,3,4,5]
k = 2
head =  createNode(head)

obj =  Solution().reverseKGroup(head,k)
LinkedListPrint(obj)