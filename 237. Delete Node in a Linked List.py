from  linkedlistfunc import LinkedListPrint , createNode
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# Find the actual node
def findNode(head, value):
    current = head

    while current:
        if current.val == value:
            return current

        current = current.next

    return None


head = [4,5,1,9]
node = 5



head = createNode(head)
node = findNode(head, node)

print("Before:")
LinkedListPrint(head)

obj = Solution()
obj.deleteNode(node)


print("After deleting 5:")
LinkedListPrint(head)