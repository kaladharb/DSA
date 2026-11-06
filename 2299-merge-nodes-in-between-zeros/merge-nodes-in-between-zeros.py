# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:


        
        left=head.next
        right=head.next
        while right:
            sumi=0

            while right.val!=0:
                sumi+=(right.val)
                right=right.next
            
            left.val=sumi
            left.next=right.next
            right=right.next
            left=left.next
        return head.next

        