class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prf=[1]*n
        prf[0]=nums[0]
        for i in range(1,n):
            prf[i]=prf[i-1]*nums[i]

        sfx=[1]*n
        sfx[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            sfx[i]=sfx[i+1]*nums[i]
    
        for i in range(n):
            if i==0:
                left=1
            else:
                left=prf[i-1]
            if i<=n-2:
                right=sfx[i+1]
            else:
                right=1

            nums[i]=left*right

        return nums




