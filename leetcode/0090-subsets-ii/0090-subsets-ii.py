class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        end = len(nums)

        ans = []

        def backtrack(start,sub):
            if sorted(sub) not in ans:
                ans.append(sorted(sub[:]))
            for i in range(start,end):
 
                sub.append(nums[i])     
                backtrack(i+1,sub)
                sub.pop()
    
     
        backtrack(0,[])
       
        return ans