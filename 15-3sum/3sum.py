class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ls=set()
        for i in range(n):
            left=i+1
            right=n-1
            
            
            while(left<right):
                sumi=nums[i]+nums[left]+nums[right]

                if sumi==0:
                    ls.add(tuple(sorted([nums[i],nums[left],nums[right]])))
                    left+=1
                    right-=1
                elif sumi<0:
                    left+=1
                else:
                    right-=1
        return list(ls)
                