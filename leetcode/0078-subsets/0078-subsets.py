class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      
        end = len(nums)

        ans = []

        def backtrack(start,sub):
            ans.append(sub[:])
            for i in range(start,end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                sub.append(nums[i])     
                backtrack(i+1,sub)
                sub.pop()
    

        backtrack(0,[])
        return ans