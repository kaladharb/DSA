class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        h=num
        fnd=False
        while(l<=h):
            mid=(l+h)//2
            res=mid * mid

            if res==num:
                fnd=True
                break
            elif res>num:
                h=mid-1
            else:
                l=mid+1
        if fnd:
            return True
        else:
            return False
