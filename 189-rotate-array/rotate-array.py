class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        def rever(nums,s,t):
            i=s
            j=t
            while(i<=j):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            return nums
        
        rever(nums,0,n-1)
        rever(nums,0,k-1)
        rever(nums,k,n-1)
        # return nums











