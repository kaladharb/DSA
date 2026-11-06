class Solution:
    def findMin(self, nums: list[int]) -> int:

        mini=float('inf')
        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2
            mini=min(mini,nums[mid])

            if nums[left]<=nums[mid]:
                mini=min(mini,nums[left])
                left=mid+1
            else:
                right=mid-1
        
        return mini


        
        