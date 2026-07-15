class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i]!=1:
        #         nums[i]=0
        cnt=0
        mp={0:1}
        pfx_s=0

        for i in nums:
            pfx_s+=(i%2)

            if pfx_s-k in mp:
                cnt+=mp[pfx_s-k]
            mp[pfx_s]=mp.get(pfx_s,0)+1
        return cnt        
        