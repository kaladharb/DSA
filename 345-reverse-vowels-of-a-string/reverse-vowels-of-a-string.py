class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        vwls="aeiouAEIOU"
        s=list(s)
        while(i<j):
            if s[i] in vwls and s[j] in vwls:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] in vwls and s[j] not in vwls:
                j-=1
            else:
                i+=1
        return ''.join(s)
                



        