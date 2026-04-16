from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        def missed_num(arr):

            m = 1
            arr = set(arr)
            while m in arr:
                m+=1
            return m
        

        missed = missed_num(nums)

        repeated = Counter(nums).most_common()[0][0]

        return [repeated,missed]

