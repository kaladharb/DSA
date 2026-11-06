class Solution:
    def findMin(self, nums: list[int]) -> int:
        mini=float('inf')

        for i in nums:
            if i<mini:
                mini=i
        return mini
        