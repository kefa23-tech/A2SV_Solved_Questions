class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

      

        remainders = {0:-1}

        cur = 0
        for i in range(len(nums)): 
            cur+=nums[i]
            remainder = cur%k
            if remainder in remainders:
                prev_idx = remainders[remainder]
                diff = i - prev_idx
                if diff >= 2:
                    return True
            else:
                remainders[remainder] = i

        return False