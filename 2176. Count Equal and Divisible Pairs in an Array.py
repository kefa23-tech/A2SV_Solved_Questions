class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        size = len(nums)
        pairs = 0
        for i in range(size):
            for j in range(i+1,size):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    pairs+=1
        return pairs
