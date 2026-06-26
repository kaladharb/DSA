class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi=0
        l=0
        r=0
        n=len(nums)
        zero=0
        while(r<n):
            if nums[r]==0:
                zero+=1
            while(zero>k):
                if nums[l]==0:
                    zero-=1
                l+=1

            if zero<=k:
                maxi=max(maxi,r-l+1)

            r+=1
        return maxi
