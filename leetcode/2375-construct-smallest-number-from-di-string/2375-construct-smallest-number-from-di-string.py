class Solution:
    def smallestNumber(self, pattern: str) -> str:
        size = len(pattern)

        stack = []

        res = ""

        for i in range(size+1):
            char = pattern[min(size-1,i)]
            stack.append(f"{i+1}")
            if char == "I":
                while stack:
                    res+=stack.pop()
        while stack:
            res+=stack.pop()
        
        return res
                