class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        for i in freq:
            if freq[i]>1:
                return i
                break
                