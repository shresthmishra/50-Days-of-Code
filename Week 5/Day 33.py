print("\n\nDay 32\n")

print("\nChallenge: Diameter of Binary Tree")
print("Context: Given the root of a binary tree, return the length of the diameter of the tree.\nThe diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.\nThe length of a path between two nodes is represented by the number of edges between them.\n\n")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Diameter:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            return 1 + max(left_height, right_height)
        height(root)
        return self.max_diameter
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Diameter()

result = solution.diameterOfBinaryTree(root)
print(f"The diameter of the binary tree is: {result}")
