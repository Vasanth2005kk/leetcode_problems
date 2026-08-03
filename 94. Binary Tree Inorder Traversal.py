from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.repass(root, result)
        return result

    def repass(self, node, result):
        if not node:
            return

        self.repass(node.left, result)
        result.append(node.val)
        self.repass(node.right, result)


# Tree: [1, None, 2, 3]
#
#      1
#       \
#        2
#       /
#      3

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

obj = Solution().inorderTraversal(root)

print(obj)