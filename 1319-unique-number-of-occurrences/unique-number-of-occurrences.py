class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1

        s=set()
        found=True
        for i in freq:
            if freq[i] in s:
                found=False
                break
            else:
                s.add(freq[i])

        if found:
            return True
        else:
            return False

