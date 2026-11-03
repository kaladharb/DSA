class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        maxi=max(nums)
        
        c=0
        for i in range(len(nums)):
            c+=maxi-nums[i]
        return c

        

        
        
        

        
        
        
         


            
            
            

