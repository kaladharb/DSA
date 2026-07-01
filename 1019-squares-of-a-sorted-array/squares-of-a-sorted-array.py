class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums.sort()
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums.sort()
        return nums
        