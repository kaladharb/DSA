# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        dummy=ListNode(0)
        dummy.next=head
        # dummy=ListNode(0,head) dummy crearte chesi dhaniki dummy next pass chesinam

        fast=dummy
        slow=dummy

        for i in range(n+1):
            fast=fast.next
        
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next

        return dummy.next

        




