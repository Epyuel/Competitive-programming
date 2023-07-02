# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_lis=[]
        while head!=None:
            if head in node_lis:
                return True
            node_lis.append(head)
            head=head.next
        return False
