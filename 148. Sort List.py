from typing import Optional
from linkedlistfunc import createNode , LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        data = []

        temp =  head
        while temp:
            data.append(temp.val)
            temp =  temp.next

        data =  sorted(data)

        temp = head
        index = 0
        while temp:
            temp.val = data[index]
            index +=1
            temp =  temp.next

        return head

head = [4,2,1,3]
head =  createNode(head)
obj =  Solution().sortList(head)

print(obj)