class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        sumi=0
        for i in nums:
            if sumi<0:
                sumi=0
            sumi+=i
            maxi=max(sumi,maxi)

        return maxi

            

       
            

            