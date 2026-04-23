from collections import defaultdict
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols, = len(grid),len(grid[0])
        islands = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(r,c):
            return 0 <= r < rows and 0 <= c <cols
        def dfs(row,col):
            # if not inbound(row,col)
            grid[row][col] = "0"

            for row_change,col_change in dirs:
                new_row,new_col = row + row_change,col + col_change
                if inbound(new_row,new_col) and grid[new_row][new_col] == "1":
                    dfs(new_row,new_col)



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands+=1
                    dfs(row,col)
        return islands

