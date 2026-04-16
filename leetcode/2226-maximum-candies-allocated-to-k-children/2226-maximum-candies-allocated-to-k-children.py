class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
    

        low = 1
        high = max(candies)
        ans = 0
        while low <= high:

            mid = (low + high) // 2

            piles = sum(i//mid for i in candies)

            if piles >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans