class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r = 0, len(matrix) -1

        while l < r:
            for i in range(r-l):
                left,right,= l,r
                initial = matrix[left][l+i]

                matrix[left][l+i] = matrix[right - i][l]

                matrix[right - i][l] = matrix[right][r - i]

                matrix[right][r-i] = matrix[left + i][r]

                matrix[left + i][r] = initial

            r-=1
            l+=1
                 
