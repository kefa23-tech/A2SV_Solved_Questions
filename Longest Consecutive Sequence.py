class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_seq = 0
        for i in s:
            if i - 1 not in s:  
            
                I = i
                while i in s:
                    i+=1
                    
                max_seq = max(max_seq,i-I)

        return max_seq
