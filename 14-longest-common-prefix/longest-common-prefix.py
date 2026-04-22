class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first_letter=strs[0]
        last_letter=strs[-1]
        n=len(first_letter)
        m=len(last_letter)
        i=0
        j=0
        new=""
        while(i<n and j<m):
            if first_letter[i]==last_letter[j]:
                new+=first_letter[i]
                i+=1
                j+=1
            else:
                break
        return new
        