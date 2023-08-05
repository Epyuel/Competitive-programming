# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.countGood=0
        def helper(node,maxVal):
            if not node:
                return
            if maxVal<=node.val:
                self.countGood+=1
            helper(node.left,max(maxVal,node.val))
            helper(node.right,max(maxVal,node.val))
        helper(root,-1*float('inf'))
        return self.countGood
