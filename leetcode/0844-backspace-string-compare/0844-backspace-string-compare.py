class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack2 = []
        for char in s:
            if stack:
                if char == "#":
                    stack.pop()
            
            if char != "#":
                    stack.append(char)
        for char in t:
            if stack2:
                if char == "#":
                    stack2.pop()
            
            if char != "#":
                    stack2.append(char)
        # print("stack",stack)
        # print("stack2",stack2)
        return stack == stack2