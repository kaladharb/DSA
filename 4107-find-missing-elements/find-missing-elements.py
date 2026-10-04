class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        ls=[]
        for i in range(mini,maxi+1):
            if i not in nums:
                ls.append(i)
        return ls
