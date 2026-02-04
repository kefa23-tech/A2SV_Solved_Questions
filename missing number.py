class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = 0
        while m in nums:
            m+=1
        return m
