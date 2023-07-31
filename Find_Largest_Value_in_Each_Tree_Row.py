# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        temp = collections.deque()
        temp.append(root)
        res = list()
        while temp:
            maxi = None
            for i in range(len(temp)):
                node = temp.popleft()
                if maxi is None or maxi < node.val:
                    maxi = node.val
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            res.append(maxi)
        return res
