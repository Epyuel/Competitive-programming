# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.count=0
        self.maxCount=0
        def helper(node):
            if not node:
                return
            self.count+=1
            self.maxCount=max(self.count,self.maxCount)
            helper(node.left)
            helper(node.right)
            self.count-=1
        
        helper(root)
        return self.maxCount
