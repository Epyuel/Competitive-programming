# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([(root, 0)])
        cur_level = 0    
        cur_level_array = []
        ans = []
        while que:
            node, level = que.popleft()
            if level == cur_level:
                cur_level_array.append(node.val)
            else:
                ans.append(cur_level_array)
                cur_level = level
                cur_level_array = [node.val]

            if node.left:
                que.append((node.left, level + 1))
            if node.right:
                que.append((node.right, level + 1))


        ans.append(cur_level_array)

        return ans
