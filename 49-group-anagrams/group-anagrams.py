class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}

        for i in strs:
            strcpy=i
            key=tuple(sorted(strcpy))

            if key not in freq:
                freq[key]=[]
            freq[key].append(i)
        
        res=[]
        for val in freq:
            res.append(freq[val])
        return res