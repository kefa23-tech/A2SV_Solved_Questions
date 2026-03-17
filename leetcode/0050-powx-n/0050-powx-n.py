class Solution:
    def myPow(self, x: float, n: int) -> float:
  
        
        if n == 0:
            return 1

        if n < 0:
            cur = 1/self.myPow(x,abs(n)) 
            return cur
        if n%2==0:
            
            cur = self.myPow(x,n//2)
            return cur * cur
        
        return x*self.myPow(x,n-1)
        
  
        

      