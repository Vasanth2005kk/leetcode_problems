from typing import Optional , List
from linkedlistfunc import createNode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        curr = head
        nums = set(nums)
        add = []
        count = 0 
        while curr:
            if curr.val in nums:
                count +=1
            else:
                if count != 0:
                    add.append(count)
                count = 0
            curr = curr.next
        if count != 0:
            add.append(count)

        # print(add)
        return len(add)

head = [3,4,0,2,1]
head =  createNode(head)
nums = [4]

obj = Solution().numComponents(head,nums)
print(obj)