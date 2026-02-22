class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        i_s = []
        j_s = []

        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                if row[j] == 0:
                    i_s.append(i)
                    j_s.append(j)
        for i in i_s:
            matrix[i] = [0]*len(matrix[i])
        for j in j_s:
            for r in range(len(matrix)):
                row = matrix[r]
                row[j] = 0
                matrix[r] = row
            


        
  
