class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        freq={}

        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        for j in freq:
            if j%2==0 and freq[j]==1:
                return j
                break
        return -1