# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum=fast=slow=ListNode(0,next=head)
        for i in range(n):
            fast=fast.next
        while(fast.next):
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dum.next
