from linkedlistfunc import createNode , LinkedListPrint
from typing import Optional , List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not nums:
            return head

        nums = set(nums)

        while head and head.val in nums:
                head = head.next

        curr = head 
        while curr and curr.next: 
            if curr.next.val in nums: 
                curr.next = curr.next.next 
            else: curr = curr.next 
        return head


nums = [1,2,3]
head = [1,2,3,4,5]

nums = [1]
head = [1,2,1,2,1,2]

head = createNode(head)

obj = Solution().modifiedList(nums,head)
LinkedListPrint(obj)

