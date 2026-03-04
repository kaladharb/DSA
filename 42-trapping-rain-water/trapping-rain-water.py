class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)

        pmax=[0]*n
        pmax[0]=height[0]
        for i in range(1,n):
            pmax[i]=max(pmax[i-1],height[i])

        smax=[0]*n
        smax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            smax[i]=max(smax[i+1],height[i])

        sumi=0
        for i in range(n):
            sumi+=min(pmax[i],smax[i])-height[i]
        return sumi