class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx=-1
        n=len(nums)
        low=0
        high=n-1

        while(low<=high):
            # mid=l+(h-l)/2
            mid=(low+high)//2
            if nums[mid]==target:
                idx=mid
                break
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return idx

