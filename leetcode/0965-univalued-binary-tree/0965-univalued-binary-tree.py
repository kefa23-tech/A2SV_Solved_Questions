# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        
        unival = root.val

        queue = deque([root])

        while queue:

            node = queue.popleft()

            if node.val != unival:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return True


























        # arr = []

        # def dfs(node):
        #     nonlocal arr
        #     if not node:
        #         return

            
        #     arr.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # if len(set(arr)) == 1:
        #     return True
        # else:
        #     return False
       