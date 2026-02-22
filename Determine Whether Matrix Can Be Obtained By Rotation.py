class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
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
            return matrix
        n = len(mat)
        for _ in range(2*n):
            
            mat = rotate(mat)
            if mat == target:
                return True
        else:
            return False
