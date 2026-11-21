class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:
        interval.sort()
        cur=interval[0]
        n=len(interval)
        res=[]
        for i in range(1,n):
            if cur[1]>=interval[i][0]:
                cur[1]=max(cur[1],interval[i][1])
            else:
                res.append(cur)
                cur=interval[i]
        res.append(cur)
        return res





        