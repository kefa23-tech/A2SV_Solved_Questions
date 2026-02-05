class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool: 
        Ranges = set()
        for nums in ranges:
            c = {n for n in range(nums[0],nums[1]+1)}
            Ranges = Ranges | c
        nwrange = {n for n in range(left,right+1)}
        return nwrange <= Ranges

        
