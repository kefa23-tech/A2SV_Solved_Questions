from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = Counter(nums)
    
        maxxes = []
        for k,v in nums.items():
            if v > n/3:
                maxxes.append(k)
        return maxxes
