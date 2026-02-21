class Solution:
    def isHappy(self, n: int) -> bool:
        def squaresums(n):
            num = 0

            while n:
                digit = n%10
                digit = digit**2
                num += digit
                n = n//10
            return num
        
        nums = set()

        while n not in nums:
            nums.add(n)
            n = squaresums(n)
            if n == 1:
                return True
        return False
