class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=float("-inf")
        mini=prices[0]
        if len(prices)==1:
            return 0
        for i in range(1,len(prices)):
            mini=min(prices[i],mini)
            ans=prices[i]-mini
            maxi=max(ans,maxi)
        return maxi