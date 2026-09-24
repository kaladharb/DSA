class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitsm(m):
            s=0
            while(m!=0):
                temp=m%10
                s+=temp
                m//=10
            return s
        
        mini=float('inf')
        for i in range(len(nums)):
            res=digitsm(nums[i])

            if res==i:
                mini=min(mini,i)
        
        if mini!=float('inf'):
            return mini
        else:
            return -1
            



            
