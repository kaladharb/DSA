class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt=0
        pfx_s=0
        mp={0:1}
        for i in nums:
            pfx_s+=i

            if pfx_s-goal in mp:
                cnt+=mp[pfx_s-goal]
            
            mp[pfx_s]=mp.get(pfx_s,0)+1
        return cnt