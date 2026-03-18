# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        def dfs(Node):

            if not Node:
                return None
            if Node.val == val:
                return Node
            elif Node.val > val:
                return dfs(Node.left)
            else:
                return dfs(Node.right)
            
        
        return dfs(root)