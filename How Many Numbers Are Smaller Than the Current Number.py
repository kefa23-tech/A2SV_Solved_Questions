class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smallers = []
        for i in nums:
            smaller = 0
            for j in nums:
                if j < i:
                    smaller+=1
            smallers.append(smaller)
        return smallers
