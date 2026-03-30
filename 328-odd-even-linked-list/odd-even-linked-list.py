# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if  head is None or head.next is None:
            return head
        od_n=head
        evn_n=head.next
        temp =evn_n
        while(evn_n is not None and evn_n.next is not None):
            
            od_n.next=evn_n.next
            od_n=evn_n.next
            evn_n.next=od_n.next
            evn_n=od_n.next
        
        od_n.next=temp

        return head



                