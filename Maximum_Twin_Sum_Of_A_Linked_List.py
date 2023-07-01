# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n=0
        dum=head
        while dum!=None:
            dum=dum.next
            n+=1

        lis=[]
        i=0
        r=0
        while head!=None:
            if ((n/2)-1) < i :
                index=n-1-i
                lis[index]=lis[index]+head.val
            else:
                lis.append(head.val)
            head=head.next
            i+=1

        s_lis=sorted(lis,reverse=True)
        return s_lis[0]
