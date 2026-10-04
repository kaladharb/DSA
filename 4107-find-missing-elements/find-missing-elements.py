class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        ls=[]
        s=set(nums)

        sumi=0
        for i in range(mini,maxi+1):
            if i not in s:
                ls.append(i)
        return ls


        