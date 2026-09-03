# from typing import Optional
# from linkedlistfunc import createNode , LinkedListPrint

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None

#         curr =  head.next
#         Btnzero = []
#         total = 0
#         while curr:
#             if curr.val != 0:
#                 total += curr.val
#             else:
#                 Btnzero.append([total,curr.next])
#                 total = 0
#             curr = curr.next

#         temp = head
#         for i in Btnzero:
#             if i[0] != 0:
#                 temp.val = i[0]
#                 temp.next = i[1]
#                 temp = temp.next


#         return head


# head = [0,3,1,0,4,5,2,0]
# # head = [0,1,0,3,0,2,2,0]

# head =  createNode(head)
# obj = Solution().mergeNodes(head)
# LinkedListPrint(obj)


from typing import Optional
from linkedlistfunc import createNode, LinkedListPrint


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head.next
        result = head
        total = 0

        while curr:

            if curr.val != 0:
                total += curr.val

            else:
                result.val = total
                total = 0

                if curr.next:
                    result.next = curr.next
                    result = result.next
                else:
                    result.next = None

            curr = curr.next

        return head


head = [0, 3, 1, 0, 4, 5, 2, 0]

head = createNode(head)

obj = Solution().mergeNodes(head)

LinkedListPrint(obj)
