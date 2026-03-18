# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        

        if not root1 and not root2:
            return None
        

        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        ans = TreeNode(v1 + v2)

        left1 = root1.left if root1 else 0
        left2 = root2.left if root2 else 0

        right1 = root1.right if root1 else 0
        right2 = root2.right if root2 else 0

        ans.left = self.mergeTrees(left1,left2)
        ans.right = self.mergeTrees(right1,right2)

        return ans

        