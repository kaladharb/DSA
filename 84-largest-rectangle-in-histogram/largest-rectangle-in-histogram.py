class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        # Enter your code here. Read input from STDIN. Print output to STDOUT
            n=len(h)
            left=[-1]*n
            right=[n]*n

            stk=[]

            for i in range(n):
                while(stk and h[stk[-1]]>=h[i]):
                    stk.pop()
                if stk:
                    left[i]=stk[-1]
                stk.append(i)
            stk=[]
            for i in range(n-1,-1,-1):
                while(stk and h[stk[-1]]>=h[i]):
                    stk.pop()
                if stk:
                    right[i]=stk[-1]
                stk.append(i)

            max_area=0
            for i in range(n):
                wid=right[i]-left[i]-1
                area=h[i]*wid
                max_area=max(max_area,area)
            return max_area


            