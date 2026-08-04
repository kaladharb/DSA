# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def rev(node):
            prev=None
            temp=node
            while(temp is not None):
                front=temp.next
                temp.next=prev
                prev=temp
                temp=front
            return prev

        slow=head
        fast=head
        while(fast.next is not None and fast.next.next is not None):
            slow=slow.next
            fast=fast.next.next
        
        scd=rev(slow.next)
        slow.next=scd

        frst=head
        scd_head=scd  #newhead got from rev
        found=True
        while(scd_head is not None):
            if frst.val !=scd_head.val:
                found=False
                break
            frst=frst.next
            scd_head=scd_head.next
        
        slow.next=rev(scd)
        return found
            
        

