class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumi=0
        n=len(mat)
        for i in range(n):
            for j in range(n):
                if i==j:
                    sumi+=mat[i][j]
                if i+j==n-1:
                    sumi+=mat[i][j]
        if n%2!=0:   
            sumi=sumi-(mat[n//2][n//2])
        return sumi
        
