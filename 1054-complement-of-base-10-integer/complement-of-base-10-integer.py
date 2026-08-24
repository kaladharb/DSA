class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res=f"{n:b}"

        new=''
        for i in range(len(res)):
            if res[i]=='0':
                new+="1"
            else:
                new+="0"
        s=0
        pwr=0
        for i in range(len(new)-1,-1,-1):
            if new[i]=='1':
                s+=2**pwr
            pwr+=1
        return s