from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = ""
        cournt = head 

        while cournt is not None :
            ans +=  str(cournt.val)
            cournt =  cournt.next

        return int(ans,2) 




l1=ListNode(1,ListNode(0,ListNode(1)))

obj = Solution().getDecimalValue(l1)
print(obj)

def print_head(head):
    cournt=head
    while cournt is not None:
        print(cournt.val,end=" -> ") 
        cournt=cournt.next


print_head(l1)
# print_head(obj)
