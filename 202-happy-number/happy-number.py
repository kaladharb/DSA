class Solution:
    def isHappy(self, n: int) -> bool:
        def sqrw(n):
            sqr=0
            while(n!=0):
                temp=n%10
                sqr+=temp**2
                n=n//10
            return sqr
        
        s=set()
        while(n!=1):
            if n in s:
                return False
            s.add(n)
            n=sqrw(n)
        return True

