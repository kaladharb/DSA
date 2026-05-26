class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumi=0
        n=len(mat)
        for i in range(n):
            sumi+=mat[i][i]
            sumi+=mat[i][n-i-1]
        
        if n%2!=0:
            sumi-=mat[n//2][n//2]
        return sumi
        
