class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # freq={}
        # for i in nums:
        #     freq[i]=freq.get(i,0)+1
        
        # for i in nums:
        #     if freq[i]>1:
        #         return True
        #         break
        #     else:
        #         return False

        s=set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return True
                break
        return False
