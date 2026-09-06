from typing import Optional
from linkedlistfunc import LinkedListPrint, createNode
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []

        curr =  head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # print("arr:",arr)
        return self.addSortedListToBST(arr)

    def addSortedListToBST(self,nums):
        if not nums:
            return None
        mid = len(nums) // 2

        root =  TreeNode(nums[mid])
        root.left = self.addSortedListToBST(nums[:mid])
        root.right = self.addSortedListToBST(nums[mid + 1:])

        return root




head = [-10,-3,0,5,9,10]

head =  createNode(head)
obj = Solution().sortedListToBST(head)

def print_tree(root, space="", is_left=True):
    if root is None:
        return

    # Print right side first
    if root.right:
        print_tree(
            root.right,
            space + ("│   " if is_left else "    "),
            False
        )

    # Print current node
    print(space + ("└── " if is_left else "┌── ") + str(root.val))

    # Print left side
    if root.left:
        print_tree(
            root.left,
            space + ("    " if is_left else "│   "),
            True)

print_tree(obj)
