class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            ships = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ships+=1
                    currCap = cap
                currCap-= w
            return ships <=days


        left,right = max(weights),sum(weights)
        res = right
        while left<=right:

            mid = (left + right) //2

            if canShip(mid):
                res = min(res,mid)
                right = mid-1
            else:
                left = mid + 1
        return res
