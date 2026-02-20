
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def is_nonZero(triangle):
            if triangle[0] + triangle[1] > triangle[2]:
                if triangle[0] + triangle[2] > triangle[1]:
                    if triangle[2] + triangle[1] > triangle[0]:
                        return True

        i = 0
        nums.sort()
        nonzeros = []
        for j in range(3,len(nums)+1):
            triangle = nums[i:j]
            if is_nonZero(triangle):
                nonzeros.append(sum(triangle))
            i+=1
        if nonzeros:
            return max(nonzeros)
        else:
            return 0
