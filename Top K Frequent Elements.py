from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums= Counter(nums)
        KEYS= nums.keys()
        vals = nums.values()
        v_k = sorted(list(zip(vals,KEYS))) 
        v_k.reverse()
        top_k  = []
        for i in range(k):
            top_k.append(v_k[i][1])

        return top_k
