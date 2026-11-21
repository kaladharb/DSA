class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)

        pfx_prd=[0]*n
        pfx_prd[0]=nums[0]
        for i in range(1,n):
            pfx_prd[i]=pfx_prd[i-1]*nums[i]
        
        sfx_prd=[0]*n
        sfx_prd[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            sfx_prd[i]=sfx_prd[i+1]*nums[i]
        
        for i in range(n):
            if i==0:
                left=1
            else:
                left=pfx_prd[i-1]
            
            if i==n-1:
                right=1
            else:
                right=sfx_prd[i+1] 
            
            res=left*right
            nums[i]=res
        return nums
        


        