class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        arr=[0]*len(nums)
        for i in range(len(nums)//2):
            arr[2*i]=pos[i]
            arr[2*i+1]=neg[i]
        return arr