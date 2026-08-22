class Solution:
    def checkDivisibility(self, n: int) -> bool:
        m=n
        sumi=0
        prd=1
        while (m!=0):
            rem=m%10
            sumi+=rem
            prd*=rem
            m//=10

        prd_ad_s=sumi+prd
        if n%prd_ad_s==0:
            return True
        else:
            return False
