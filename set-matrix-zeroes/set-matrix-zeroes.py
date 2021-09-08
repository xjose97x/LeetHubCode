class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowZero = False
        firstColZero = False
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        firstRowZero = True
                    if col == 0:
                        firstColZero = True
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1, m):
            for col in range(1, n):
                if 0 in (matrix[row][0], matrix[0][col]):
                    matrix[row][col] = 0
                    
        if firstRowZero:
            for col in range(n):
                matrix[0][col] = 0
        
        if firstColZero:
            for row in range(m):
                matrix[row][0] = 0
                
