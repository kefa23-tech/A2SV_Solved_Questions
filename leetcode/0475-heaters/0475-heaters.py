import bisect
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        max_ = -1
        heaters.sort()
        for house in houses:
            i = bisect.bisect_left(heaters,house)
        
            left = i-1
            right = i

            left_dist = house - heaters[left] if i > 0 else float("inf")
            right_dist =heaters[right] - house if i < len(heaters) else float("inf")
            closest = min(left_dist,right_dist)
            max_ = max(max_,closest)
        #print(pos)
        return max_