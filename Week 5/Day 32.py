print("\n\nDay 31\n")

print("\nChallenge: Sum of Left Leaves")
print("Context: Given the root of a binary tree, return the sum of all left leaves.\nA leaf is a node with no children. A left leaf is a leaf that is the left child of another node.\n\n")

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Lefts:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total = 0
        
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        
        return total

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Lefts()

result = solution.sumOfLeftLeaves(root)
print(f"The sum of left leaves in the tree is: {result}")
