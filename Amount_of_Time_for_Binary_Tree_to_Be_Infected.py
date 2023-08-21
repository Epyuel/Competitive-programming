# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        graph = defaultdict(list)
        ans = 0

        def build_graph(node, parent):
            graph[node.val].append(parent)
            if node.left:
                graph[node.val].append(node.left.val)
                build_graph(node.left, node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                build_graph(node.right, node.val)
        
        def get_depth(node, parent, depth):
            nonlocal ans
            ans = max(ans, depth)
            for nei in graph[node]:
                if nei != parent:
                    get_depth(nei, node, depth + 1)

        if root:
            if root.left:
                graph[root.val].append(root.left.val)
                build_graph(root.left, root.val)
            if root.right:
                graph[root.val].append(root.right.val)
                build_graph(root.right, root.val)
                    
            get_depth(start, -1, 0)

        return ans
