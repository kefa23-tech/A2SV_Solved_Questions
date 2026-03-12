class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        
    
        stack = [0]
    

        for char in s:
            if char == "(":
                stack.append(0)
                # print("stack",stack)

            else:
                # print(len(stack))
                val = stack.pop()
                score = max(1,2*val)
                stack[-1]+=score
             

        # print(stack)
        return stack[-1]
                