class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        x = min(nums)
        left = 0
        right = len(nums)-1
        min_ = float("inf")
        while left <= right:
            mid = (left + right) // 2
            if left == right:
                return nums[mid]
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid

            # print("l", left, "r", right)
            # if nums[mid - 1] > nums[mid] < nums[(mid + 1) % n]:
            #     return nums[mid]
            # elif nums[(mid + 1 % n)] < nums[mid ]:
            #     left = mid + 1
            # elif nums[mid - 1] < nums[mid]:
            #     right = mid - 1
            # if right == -1:
            #     right = n -1
            #     left = (left + right) // 2
            # print("mid",mid,nums[mid])
            
            # if nums[mid] == x:
            #     return x
        # return min_