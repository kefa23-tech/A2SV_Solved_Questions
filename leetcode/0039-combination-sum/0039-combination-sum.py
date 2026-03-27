class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # get the subsets and if the sum == target add the sub to ans

        ans = []

        def dfs(i,cur,total):
            if total == target:
                ans.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            
            # include i          
            dfs(i,cur,total+candidates[i])
            cur.pop()

            # disinclude i

            dfs(i+1,cur,total)
        
        dfs(0,[],0)

        return ans