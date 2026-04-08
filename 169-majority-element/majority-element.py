class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele=0
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                ele=nums[i]
                cnt=1
            elif ele==nums[i]:
                cnt+=1
            else:
                cnt-=1
        cnt1=0
        for i in nums:
            if i==ele:
                cnt1+=1
        if cnt1>len(nums)//2:
            return ele
        else:
            return -1