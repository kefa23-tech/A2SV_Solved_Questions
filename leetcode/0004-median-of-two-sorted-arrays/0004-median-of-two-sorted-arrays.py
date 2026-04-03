class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1+=nums2
        nums1.sort()

        if len(nums1)%2:
            mid = len(nums1) // 2
            return nums1[mid]
        mid_right = len(nums1)//2
        mid_left = mid_right - 1
        total = nums1[mid_left] + nums1[mid_right]

        return total / 2