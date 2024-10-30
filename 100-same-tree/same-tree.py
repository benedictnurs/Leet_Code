# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        t1 = []
        t2 = []

        def dfs(root, arr):
            if root is None:
                arr.append("!")
                return
            arr.append(root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)

        dfs(p,t1)
        dfs(q,t2)
        print(t1, t2)

        return t1 == t2

