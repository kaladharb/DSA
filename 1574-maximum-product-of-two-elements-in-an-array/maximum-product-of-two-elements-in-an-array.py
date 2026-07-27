class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=0
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    prd=(nums[i]-1)*(nums[j]-1)
                    maxi=max(prd,maxi)
        return maxi