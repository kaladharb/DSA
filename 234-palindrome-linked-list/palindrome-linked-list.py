# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=head
        ls=[]
        while (temp is not None):
            ls.append(temp.val)
            temp=temp.next
        
        temp2=head
        fd=True
        while temp2 is not None and len(ls)!=0:
            if temp2.val!=ls.pop():
                fd=False
                break
            
            temp2=temp2.next

        if fd:
            return True
        else:
            return False




        