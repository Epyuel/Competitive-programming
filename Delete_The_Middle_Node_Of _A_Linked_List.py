# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        temp=head
        while temp!=None:
            temp=temp.next
            n+=1
        if n==0 or n==1:
            return None

        dummy=ListNode(0,head)
        for i in range(n//2):
            dummy=dummy.next

        dummy.next=dummy.next.next
        return head
