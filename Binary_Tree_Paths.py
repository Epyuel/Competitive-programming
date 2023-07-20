# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=""
        self.result=[]
        def helper(node,res):
            if not node:
                return
            if not (node.right) and not (node.left):
                res+=f"{node.val}"
                self.result.append(res)
                res=""
                return

            res+=f"{node.val}->"
            helper(node.left,res)
            helper(node.right,res)

        helper(root,res)
        return self.result
