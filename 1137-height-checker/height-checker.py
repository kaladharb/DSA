class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_he=heights[:]
        heights.sort()
        count=0
        for i in range(len(heights)):
            if heights[i]!=new_he[i]:
                count+=1
        return count

            

        
