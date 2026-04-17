from bisect import bisect_left,bisect_right
class Solution:
    def createSortedArray(self, nums: List[int]) -> int:

        ans = 0
        Mod = 10**9 + 7
        sorted_lis = []

        for num in nums:

            left = bisect_left(sorted_lis,num)
            
            right = bisect_right(sorted_lis,num)

            #print(left,right)
            
            #print(sorted_lis)
            # if sorted_lis[-1] == sorted_lis[right-1]:
            #     continue
            
            ans+= min(left,len(sorted_lis) - right) 
            ans%=Mod
            sorted_lis.insert(left,num)
        
        return ans
            
        