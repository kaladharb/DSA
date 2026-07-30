class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)

        s=0
        if n<=8:
            s+=n
        elif n<=16:
            x=n-8
            s+=8
            s+=x*2
        elif n<=24:
            s+=8
            s+=16
            z=n-16
            s+=z*3
        else:
            s+=8 + 16 + 24 + (n - 24) * 4
        return s




