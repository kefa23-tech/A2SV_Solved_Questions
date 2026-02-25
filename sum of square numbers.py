from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        

        left,right = 0,int(sqrt(c))

        while left <= right:
            a = left
            b = right
            two_square = a*a + b*b 
            mid = (left + right)//2
            if two_square == c:
                return True
            elif two_square > c:
                right-=1
            else:
                left+=1
        return False
