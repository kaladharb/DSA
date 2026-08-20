class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        sk=[]
        new=[0]*n
        
        for i in range(n-1,-1,-1):

            while len(sk)!=0 and temperatures[sk[-1]]<=temperatures[i]:
                sk.pop()
        

            if len(sk)!=0:
                new[i]=sk[-1]-i

            sk.append(i)
        return new





        
