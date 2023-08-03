# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth=0
        def helper(node,currDepth):
            if not node:
                return
            currDepth+=1
            self.maxDepth= max(currDepth,self.maxDepth)
            helper(node.left,currDepth)
            helper(node.right,currDepth)
        
        helper(root,0)
        return self.maxDepth
