class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # find the row
        def findRow(matrix):
            j = len(matrix)

            left = 0 
            right = j-1

            while left <= right:
                mid = (left + right) // 2

                if matrix[mid][0] <= target:
                    if matrix[right][0] <= target:
                        return right
                    else:
                        left = mid+1
                if matrix[mid][0] > target:
                    right = mid-1

            return right
        
        row = findRow(matrix)
        #print(row)
        
        left = 0
    
        row = matrix[row]
        right = len(row)-1
        
        print(row)
        
        while left <= right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        

                    