class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)+1
        prf_arr=[0]*n
        prf_arr[0]=0
        for i in range(1,n):
            prf_arr[i]=prf_arr[i-1]+gain[i-1]
        
        res=max(prf_arr)
        return res

