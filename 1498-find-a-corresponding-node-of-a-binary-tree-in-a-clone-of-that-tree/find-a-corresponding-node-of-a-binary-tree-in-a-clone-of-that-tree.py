# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def recur(original, cloned, target):
            if original:
                if original == target:
                    return cloned
                else:
                    left = recur(original.left, cloned.left, target)
                    right = recur(original.right, cloned.right, target)

                    return left or right
                    
        return recur(original, cloned, target)
