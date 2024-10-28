# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        data = [True]

        def search(root):
            if not root:
                return 0
            left = search(root.left)
            right = search(root.right)
            if abs(left - right) > 1:
                data[0] = False
                return 0 
            return 1 + max(right, left)
        search(root)
        
        return data[0]