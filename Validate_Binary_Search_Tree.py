# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag=False
        def helper(node,lb,ub):
            if not node:
                return True
            if not(lb < node.val < ub):
                return False
            

            l=helper(node.left,lb,node.val)
            r=helper(node.right,node.val,ub)
            return l and r

        return helper(root,-1*float('inf'),float('inf'))

            
