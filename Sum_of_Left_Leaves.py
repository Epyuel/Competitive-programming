# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def recurr(temp, isLeft):
            if not temp:
                return 0
            if not temp.left and not temp.right and isLeft:
                return temp.val
            return recurr(temp.left, True) + recurr(temp.right, False)
        
        return recurr(root, False)
