class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        pfx=1
        sfx=1
        maxi_ele=float("-inf")
        for i in range(n):
            pfx*=nums[i]
            sfx*=nums[n-1-i]
            maxi_ele=max(maxi_ele,pfx,sfx)

            if pfx==0:
                pfx=1
            if sfx==0:
                sfx=1
        return maxi_ele