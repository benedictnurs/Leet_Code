# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        
        sol = 0
        q = deque([root])

        while q:
            sol = 0
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                sol += (node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        
        return sol




            