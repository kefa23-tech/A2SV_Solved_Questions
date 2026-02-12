class Solution:
    def frequencySort(self, s: str) -> str:
        new_s = ""
        uni = list(set(s))
        freq = []
        for i in uni:
            c= s.count(i)
            freq.append((c,i))
        freq.sort(reverse=True)
        for f,ch in freq:
            new_s+=ch*f
        return new_s
     

