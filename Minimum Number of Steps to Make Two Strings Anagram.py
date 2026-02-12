from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = Counter(s)
        t = Counter(t)
        ans = 0
        for char,count in s.items():
            if char in t:
                difference = count- t[char]
                ans+= max(0,difference)
            else:
                ans+=count
        return ans
