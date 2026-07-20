class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        
        found=True
        for i in freq:
            for j in freq:
                if freq[i]==freq[j] and i!=j:
                    found=False
                    break

        if found:
            return True
        else:
            return False

