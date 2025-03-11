from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left, right, level):
            if not left or not right:
                return
            if level % 2 == 0:
                right.val, left.val = left.val,right.val
            
            dfs(left.left, right.right, level + 1)
            dfs(left.right, right.left, level + 1)
        
        dfs(root.left, root.right, 0)
        return root