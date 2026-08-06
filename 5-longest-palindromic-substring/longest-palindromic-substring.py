class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi=0
        n=len(s)
        strt=0
        ans=""
        for i in range(n):
            l=i
            r=i
            while(l>=0 and r<n):
                if s[l]==s[r]:
                    l-=1
                    r+=1
                else:
                    break
            if (r-l-1)>maxi:
                maxi=r-l-1
                ans=s[l+1:r]

            l=i
            r=i+1
            while(l>=0 and r<n):
                if s[l]==s[r]:
                    l-=1
                    r+=1
                else:
                    break
            if (r-l-1)>maxi:
                maxi=r-l-1
                ans=s[l+1:r]

        return ans
        
        


                


           