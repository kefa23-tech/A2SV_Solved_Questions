# from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefix_sum = 0

        remainders = defaultdict(int)
        ans = 0
        remainders[0] = 1
        for num in nums:
            prefix_sum+=num

            remainder = prefix_sum % k
            if remainder in remainders:
                ans+=remainders[remainder]
            remainders[remainder] +=1
        return ans

