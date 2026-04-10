class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ls=[]
        mp={}
        mini=(len(nums)//3)+1
        for i in nums:
            mp[i]=mp.get(i,0)+1
            if mp[i]==mini:
                ls.append(i)
            if len(ls)==2:
                break
        return ls