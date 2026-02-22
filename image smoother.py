
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        # create a result zeor matrix with the same size
        res = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                total_sum = 0
                count = 0 
                 # select a 3X3 sub matrix and calculate total and count
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        #check if the neighboring elment is in the boundary
                        if 0 <= i and i < rows and 0 <= j and j < cols:
                            total_sum += img[i][j]
                            count += 1
                res[r][c] = total_sum // count
                
        return res
