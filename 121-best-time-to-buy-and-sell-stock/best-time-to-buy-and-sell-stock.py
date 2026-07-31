class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        mini=float('inf')
        for i in prices:
            mini=min(i,mini)
            res=i-mini
            maxi=max(res,maxi)
        return maxi
       