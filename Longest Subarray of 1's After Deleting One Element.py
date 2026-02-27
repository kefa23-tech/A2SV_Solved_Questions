class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        

        maxx = 0
        left = 0
        zero = -1
        
        for right in range(len(nums)):
            if nums[right] == 0:
                left = zero+1
                zero = right
            maxx = max(maxx,right- left)
        
    
        return maxx
