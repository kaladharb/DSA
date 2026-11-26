class Solution:
    def canAliceWin(self, n: int) -> bool:
        al=True
        alc=10

        while(n>=alc):
            n-=alc
            alc-=1

            if al==True:
                al=False
            else:
                al=True
        
        if al==True:
            return False
        else:
            return True



