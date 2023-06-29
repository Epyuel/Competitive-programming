# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        odd=head
        even=odd.next
        even_h=even
        odd_h=odd
        # odd_l=None
        o_index=0
        e_index=0
        while even and odd:
            if o_index<=e_index:
                odd.next=even.next
                o_index+=1
                odd=odd.next
            else:
                even.next=odd.next
                e_index+=1
                even=even.next
        while odd_h.next:
            odd_h=odd_h.next
        odd_h.next=even_h
        return head
