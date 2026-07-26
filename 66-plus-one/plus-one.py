class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s=""
        for i in digits:
            s+=str(i)
        res=1+int(s)

        ar=[]
        for i in str(res):
            ar.append(int(i))
        return ar