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
        p=0
        n=0
        for i in range(len(nums)):
            # arr[2*i]=pos[i]
            # arr[2*i+1]=neg[i]
            if i%2==0:
                arr[i]=pos[p]
                p+=1
            else:
                arr[i]=neg[n]
                n+=1
        return arr