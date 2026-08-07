# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while(temp is not None):
            arr.append(temp.val)
            temp=temp.next
        
        arr.sort()
        temp1=head
        for i in range(len(arr)):
            temp1.val=arr[i]
            temp1=temp1.next
        return head
        