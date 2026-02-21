class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patt = {}
        for i in range(len(pattern)):
            char = pattern[i]
            if char not in patt:
                patt[char] = [i]
            elif char in patt:
                patt[char].append(i)
        pat = {}
        s = list(s.split())
        # print(s)
        for i in range(len(s)):
            char = s[i]
            if char not in pat:
                pat[char] = [i]
            elif char in pat:
                if i % len(s) not in pat[char]:
                    pat[char].append(i)
        # print(patt.values())
        # print(patt.keys())
        # print(pat.values())
        return list(patt.values()) == list(pat.values())
            
            
