class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0]*(len(s)+1)
        for start,end,direction in shifts:
            shift = 1 if direction == 1 else -1
            diff[start] += shift
            diff[end+1] -=shift
        net = [0]*len(s)
        cur = 0

        for i in range(len(s)):
            cur+=diff[i]
            net[i] = cur
        res = []
        for i in range(len(s)):
            pos = ord(s[i]) - ord("a")
            new_pos = (pos + net[i])%26
            res.append(chr(new_pos + ord("a")))
        return "".join(res)