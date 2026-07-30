# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        temp=head
        count=0
        while(temp is not None):
            temp=temp.next
            count+=1
        
        lgn=count//2

        temp=head
        for i in range(lgn-1):
            temp=temp.next
        if temp and temp.next:
            temp.next=temp.next.next

        return head








        # slow=head
        # fast=head
        # prev=None

        # while(fast is not None and fast.next is not None):
        #     prev=slow
        #     slow=slow.next
        #     fast=fast.next.next

        # prev.next=slow.next

        # return head

        
        