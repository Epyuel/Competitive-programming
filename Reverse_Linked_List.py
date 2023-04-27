class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev
        return self.head
