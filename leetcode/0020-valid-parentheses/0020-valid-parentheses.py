class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        parentheses = {")":"(",
                    "}":"{",
                    "]":"[",}

        if s[0] in parentheses:
            return False
        
        for char in s:
            if char not in parentheses:
                stack.append(char)
            else:
                if stack:
                    if stack[-1] == parentheses[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return stack == []

