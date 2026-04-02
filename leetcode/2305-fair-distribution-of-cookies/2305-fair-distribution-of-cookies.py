class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        min_unfair = float("inf")

        distr = [0]*k

        def backtrack(i):
            nonlocal min_unfair
            if i == len(cookies):
                min_unfair = min(min_unfair,max(distr))
                return
            
            if min_unfair <= max(distr):
                return
            
            for j in range(k):
                distr[j] +=cookies[i]
                backtrack(i+1)
                distr[j]-=cookies[i]
            
        backtrack(0)
        return min_unfair
