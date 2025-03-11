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
        if not root:
            return None
        
        q = deque([root])
        curr = 0
        
        while q:
            level_size = len(q)
            level_nodes = []
            
            for _ in range(level_size):
                node = q.popleft()
                level_nodes.append(node)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if curr % 2 != 0:
                left, right = 0, len(level_nodes) - 1
                while left < right:
                    level_nodes[left].val, level_nodes[right].val = level_nodes[right].val, level_nodes[left].val
                    left += 1
                    right -= 1
            
            curr += 1
        
        return root
