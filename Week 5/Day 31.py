print("\n\nDay 31\n")

print("\nChallenge: Minimum Depth of Binary Tree")
print("Context: Given a binary tree, find its minimum depth.\nThe minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.\nNote: A leaf is a node with no children.\n\n")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class DepthofBT:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = DepthofBT()

result = solution.minDepth(root)
print(f"The minimum depth of the tree is: {result}")