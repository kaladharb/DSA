class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        self.pfx=[0]*n
        self.pfx[0]=nums[0]
        for i in range(1,n):
            self.pfx[i]=self.pfx[i-1]+nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.pfx[right]
        else:
            return self.pfx[right]-self.pfx[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)