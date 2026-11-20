class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chrs=set()
        l=0
        r=0
        n=len(s)
        lng=0
        while r<n:
            while s[r] in chrs:
                chrs.remove(s[l])
                l+=1

            chrs.add(s[r])
            lng=max(len(chrs),lng)
            r+=1
        return lng