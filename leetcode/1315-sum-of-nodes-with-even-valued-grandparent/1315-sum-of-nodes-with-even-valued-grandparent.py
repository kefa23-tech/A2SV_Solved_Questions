# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        self.total = 0

        def dfs(child,parent,granpa):

            if not child:
                return
            
            if granpa and granpa % 2 == 0:
                self.total+= child.val
            
            dfs(child.left,child.val,parent)
            dfs(child.right,child.val,parent)
        
        dfs(root,None,None)

        return self.total