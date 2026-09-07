class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls=[]
        n=len(s)
        mp1={}
        
        for i in p:
            mp1[i]=mp1.get(i,0)+1

        mp2={}
        left=0
        for right in range(n):
            mp2[s[right]]=mp2.get(s[right],0)+1

            while right-left+1 > len(p):
                
                mp2[s[left]] -= 1

                if mp2[s[left]]==0:
                    del mp2[s[left]]
                left+=1
            
            if mp1==mp2:
                ls.append(left)
        return ls




