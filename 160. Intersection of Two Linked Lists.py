from typing import Optional
from linkedlistfunc import LinkedListPrint
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        head1 = headA
        head2 = headB

        while(head1 != head2):
            head1 =  head1.next
            head2 =  head2.next
            if head1 == head2:
                return head1

            if head1 == None:
                head1 = headB
            if head2 == None:
                head2 = headA

        return head1 


print("========== TEST CASE 1 ==========")

# Create common nodes
common1 = ListNode(8)
common2 = ListNode(4)
common3 = ListNode(5)

common1.next = common2
common2.next = common3

# Create List A
a1 = ListNode(4)
a2 = ListNode(1)

a1.next = a2
a2.next = common1

# Create List B
b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(1)

b1.next = b2
b2.next = b3
b3.next = common1


# Print lists
print("List A:")
LinkedListPrint(a1)

print("List B:")
LinkedListPrint(b1)

intersection = Solution().getIntersectionNode(a1, b1)
if intersection is not None:
    print("Intersection:", intersection.val)
else:
    print("No Intersection")