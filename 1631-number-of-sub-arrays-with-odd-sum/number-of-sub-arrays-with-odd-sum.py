class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans=0
        ps=0
        ev=1
        od=0
        mod=10**9 +7

        for i in arr:
            ps+=i
            if ps%2==0:
                ans+=od
                ev+=1
            else:
                ans+=ev
                od+=1
        return ans%mod
                
