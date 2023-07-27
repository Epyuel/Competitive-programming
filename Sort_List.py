# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        res = []
        curr = head
        while curr:
            res.append(curr)
            curr = curr.next
        res.sort(key=lambda x: x.val)
        for i in range(1, len(res)):
            res[i - 1].next = res[i]
        res[len(res) - 1].next = None
        return res[0]
