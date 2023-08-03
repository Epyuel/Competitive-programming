# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        treeP=[]
        treeQ=[]
        def helper(node,tree):
            if not node:
                tree.append(node)
                return
            tree.append(node.val)
            helper(node.left,tree)
            helper(node.right,tree)
        
        helper(p,treeP)
        helper(q,treeQ)

        if treeQ == treeP:
            return True
        return False
