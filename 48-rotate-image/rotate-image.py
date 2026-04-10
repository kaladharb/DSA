class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        ans=[[0]*n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                ans[j][n-1-i]=matrix[i][j]
        
        for i in range(n):
            for j in range(m):
                matrix[i][j]=ans[i][j]

        return matrix