class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        n=len(nums)
        for i in range(2**n):
            ls=[]
            for j in range(n):
                if (i&(1<<j))==0:
                    ls.append(nums[j])
            subset.append(ls)
        return subset