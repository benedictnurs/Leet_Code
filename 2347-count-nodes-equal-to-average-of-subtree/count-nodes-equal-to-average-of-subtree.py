# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        total = 0
        def dfs(node):
            if node is None:
                return (0,0)

            lsum, ltotal = dfs(node.left)
            rsum, rtotal = dfs(node.right)
            
            tsum = lsum + rsum + node.val
            ttotal = ltotal + rtotal + 1
            nonlocal total
            if (node.val == tsum // ttotal):
                total += 1
            return (tsum, ttotal)
        dfs(root)
        return total