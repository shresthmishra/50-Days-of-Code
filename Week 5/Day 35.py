print("\n\nDay 35\n")

print("\nChallenge: Binary Tree Level Order Traversal")
print("Context: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).")

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []      
        result = []
        queue = deque([root])      
        while queue:
            level_size = len(queue)
            current_level = []  
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()

level_order_result = solution.levelOrder(root)
print(f"The level order traversal of the tree is: {level_order_result}")
