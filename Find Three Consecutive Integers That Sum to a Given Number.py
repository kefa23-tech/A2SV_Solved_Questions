class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        i = 3
        
        mod = 0
    
        if num % 3 == 0:
            x= num // 3
            return [x-1,x,x+1]
        else:
            return []
