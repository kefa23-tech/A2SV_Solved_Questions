import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in set(nums):
            return [-1,-1]
        first = bisect.bisect_left(nums,target)
        last = bisect.bisect_right(nums,target)

        return [first,last-1]