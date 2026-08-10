from typing import Optional
from linkedlistfunc import createNode , LinkedListPrint
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        headDats = []
        while temp:
            # print(temp.val)
            headDats.append(temp.val)
            temp =  temp.next

        headDats =  sorted(headDats)

        temp = head
        index = 0
        while temp:
            temp.val = headDats[index]
            index +=1
            temp = temp.next

        # print(headDats)
        # LinkedListPrint(head)
        return head

head = [4,2,1,3]
head = createNode(head)
obj = Solution().insertionSortList(head)

print(obj)