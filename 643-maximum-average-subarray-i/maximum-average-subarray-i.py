class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi=float('-inf')
        n=len(nums)
        l=0
        r=0
        sumi=0
        while r<n:
            
            if (r-l+1>k):
                sumi-=nums[l]
                l+=1
            
            sumi+=nums[r]
            if r-l+1==k:
                avg=sumi/k
                maxi=max(round(avg,5),maxi)
            r+=1
        return maxi
        
            