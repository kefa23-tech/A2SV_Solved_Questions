class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)

        while left < right and top < bottom :
            # append the upper section
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1 # make the top one step down

            # append the all the right most elements

            for i in range(top,bottom):
                res.append(matrix[i][right -1])
            right-=1 # make the bottom one step up

            # check if the spiral is done or not 
            if not (left < right and top < bottom):
                break

            # append all the bottom elements right to left

            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])

            bottom-=1 # make the left one step back


            # append all the left most elements

            for i in range(bottom -1, top-1,-1):
                res.append(matrix[i][left])
            left+=1 #make the left one step forward
        return res






        
