class Solution:
    def fib(self, n: int) -> int:
        # the state is n ( we check the state of n)
        # base cases
        
        if n == 1:
            return 1
        if n == 0:
            return 0
        
        return self.fib(n-1) + self.fib(n-2)# recurunce relation