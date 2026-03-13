class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        temp=[]
        for j in freq:
            temp.append([freq[j],j])
        temp.sort(key=lambda x:(x[0], -x[1]))
        new=[]
        for key in temp:
            for _ in range(key[0]):
                new.append(key[1])
        return new

    