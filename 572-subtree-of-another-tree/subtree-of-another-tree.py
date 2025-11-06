# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def same(q,p):
            if q is None and p is None:
                return True
            if q is None or p is None or p.val != q.val:
                return False
            return same(p.left,q.left) and same(p.right, q.right)
        
        def dfs(node):
            if not node:
                return False
            if same(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)