class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        j=n-1
        while(i<j):
            k=numbers[i]+numbers[j]
            if k==target:
               return [i+1,j+1]
            elif k>target:
                j-=1
            else:
                i+=1
        return res