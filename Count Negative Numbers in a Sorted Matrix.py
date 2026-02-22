
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        nums = []
        for row in grid:
            nums.extend(row)
        nums.sort()
        n = 0
        for i in nums:
            if i < 0:
                n+=1
        return n

        
