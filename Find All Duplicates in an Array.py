from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        res = []
        for k,v in nums.items():
            if v > 1:
                res.append(k)
        return res
