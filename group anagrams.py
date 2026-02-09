from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        # for i in range(len(strs)):
        #     anagram = []
        #     for j in range(len(strs)):
        #         if sorted(list(strs[i])) == sorted(list(strs[j])):
        #             anagram.append(strs[j])
        #     print(anagram)
        #     if anagram not in res:
        #         res.append(anagram)
        s = [sorted(list(word)) for word in strs ]
        sds = {}
        for k,v in enumerate(s):
            sds["".join(v)] = []
        for word in strs:
            sds["".join(sorted(list(word)))].append(word)
        for anagram in sds:
            res.append(sds[anagram])
        
        return res
