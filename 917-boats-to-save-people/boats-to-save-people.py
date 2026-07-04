class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        low=0
        right=n-1
        people.sort()
        boat=0
        while(low<=right):
            if people[low]+people[right]<=limit:
                boat+=1
                low+=1
                right-=1
            else:
                boat+=1
                right-=1
        return boat



        
        