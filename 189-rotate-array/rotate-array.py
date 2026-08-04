class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i=0
        n=len(nums)
        k%=n
        arr=[0]*n
        for p in range(n-k,n):
            arr[i]=nums[p]
            i+=1
        for j in range(n-k):
            arr[i]=nums[j]
            i+=1
        nums[:] =arr
        # return nums

        


            
