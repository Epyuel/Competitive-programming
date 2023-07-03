# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.left = []
        def dfs(node):
            a = node.next
            self.left.append(node.val)
            if a is not None:
                dfs(a)
        dfs(head)
        left = self.left
        g = max(left)
        p = []
        a = left[-1]
        for i in range(len(left)-2,-1,-1):
            if left[i]>=a:
                p.append(left[i])
                a = left[i]
        p.insert(0,left[-1])
        f = p[::-1]
        new = ListNode(f.pop(0))
        current = new
        while f:
            current.next = ListNode(f.pop(0))
            current = current.next
        return new
