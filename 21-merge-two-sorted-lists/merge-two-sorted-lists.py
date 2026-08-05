# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        temp=dummy
        frst=list1
        secd=list2
        while(frst is not None and secd is not None):
            if frst.val<=secd.val:
                temp.next=frst
                frst=frst.next
            else:
                temp.next=secd
                secd=secd.next
            temp=temp.next
        
        while(frst is not None):
            temp.next=frst
            frst=frst.next
            temp=temp.next
        while(secd is not None):
            temp.next=secd
            secd=secd.next
            temp=temp.next
        return dummy.next
