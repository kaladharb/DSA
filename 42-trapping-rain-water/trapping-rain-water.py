class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)

        psh=[0]*n
        psh[0]=height[0]
        for i in range(1,n):
            psh[i]=max(psh[i-1],height[i])
        
        sfh=[0]*n
        sfh[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            sfh[i]=max(sfh[i+1],height[i])
        
        sumi=0
        for i in range(n):
            sumi+=min(psh[i],sfh[i])-height[i]
        return sumi