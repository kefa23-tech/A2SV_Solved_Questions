from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
     
        counts = Counter(s)

        ans = []
        for char in order:
            if char in counts:
                ans.append(char*counts[char])
                del counts[char]
        for char,count in counts.items():
            ans.append(char*count)
        return "".join(ans)
