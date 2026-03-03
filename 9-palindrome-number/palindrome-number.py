class Solution:
    def isPalindrome(self,n:int)->bool:
        if n<0:
            return False
        rev=0
        org=n
        while(n>0):
            rev = rev*10+(n%10)
            n=n//10
        if rev==org:
            return True
        else:
            return False
