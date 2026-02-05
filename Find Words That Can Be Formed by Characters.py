from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        goods = []
        res = 0
     
        for word in words:
            good = True
            Chars = Counter(chars)
            for char in word:
                if char not in chars or Chars[char] == 0:
                    good = False
                    break
                else:
                    Chars[char]-=1
            if good:
                res += len(word)
                # goods.append(word)
                # print(word)

        # res = "".join(goods)
        return res
