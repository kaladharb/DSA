class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sumi=0
        maxi=float('-inf')
        for i in nums:
            if sumi<0:
                sumi=0
            sumi+=i
            maxi=max(sumi,maxi)
        return maxi

            