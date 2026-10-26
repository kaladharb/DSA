class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        n=len(nums)
        new=[0]*n
        for i in range(n):
            c=0
            for j in range(n):
                if i!=j and nums[i]>nums[j]:
                    c+=1
            new[i]=c
        return new