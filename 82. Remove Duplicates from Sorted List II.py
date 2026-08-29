from typing import Optional
from linkedlistfunc import createNode, LinkedListPrint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dubliacteData = {}

        # Count each value
        temp = head
        while temp:
            if temp.val not in dubliacteData:
                dubliacteData[temp.val] = 1
            else:
                dubliacteData[temp.val] += 1

            temp = temp.next


        # Find how many unique values exist
        count = 0
        for i in dubliacteData:
            if dubliacteData[i] == 1:
                count += 1

        # No unique values
        if count == 0:
            return None

        # Relink the nodes
        dummy = ListNode(0)
        current = dummy
        temp = head

        while temp:
            if dubliacteData[temp.val] == 1:
                current.next = temp
                current = current.next

            temp = temp.next

        # End the new linked list
        current.next = None

        return dummy.next

head = [1,2,3,3,4,4,5]
head = createNode(head)

obj = Solution().deleteDuplicates(head)
LinkedListPrint(obj)



'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:

            # Duplicate found
            if current.next and current.val == current.next.val:

                duplicate = current.val

                # Skip all nodes with this value
                while current and current.val == duplicate:
                    current = current.next

                prev.next = current

            else:
                # Current value is unique
                prev = current
                current = current.next

        return dummy.next
'''