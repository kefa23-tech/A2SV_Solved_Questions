from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        ref = Counter(s1)
        perm = Counter()
        left = 0
        for right in range(len(s1)):

            perm[s2[right]]+=1
        if perm == ref:
            return True
        
        for right in range(len(s1),len(s2)):
            perm[s2[right]] +=1
            perm[s2[left]] -=1

            if perm[s2[left]] < 0:
                del perm[s2[left]]
            left+=1
  
            if perm == ref :
                return True
        return False

