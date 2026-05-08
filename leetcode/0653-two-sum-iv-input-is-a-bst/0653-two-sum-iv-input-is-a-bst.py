# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        nums = []
        def dfs(node):
            nonlocal nums
            if not node:
                return
            
            nums.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)


        d ={}

        for i in range(len(nums)):
            if k - nums[i] in d:
                return True
            d[nums[i]] = i
        return False