class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        
        me = 0
        size = len(piles)
        size = size - size // 3
        for i in range(1,size,2):
            me+=piles[i]

        return me
