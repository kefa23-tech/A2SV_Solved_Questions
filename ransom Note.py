from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        # for char,count in magazine.items():
        #     if char not in ransomNote:
        #         return False
        return ransomNote <= magazine

        
