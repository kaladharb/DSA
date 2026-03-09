class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=0
        final_ele=0
        for i in nums:
            if majority==0:
                final_ele=i
                majority=1
            elif final_ele==i:
                majority+=1
            else:
                majority-=1
        return final_ele     