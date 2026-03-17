class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        evens = pow(5,n//2,mod)
        primes = pow(4,n//2,mod)
        ans = pow(5,n%2)

        return evens*primes*ans % mod

        
        evens = n//2
        primes = n//2
        ans = pow(5,evens,mod) * pow(4,primes,mod) * pow(n%2)

        return ans % mod


        