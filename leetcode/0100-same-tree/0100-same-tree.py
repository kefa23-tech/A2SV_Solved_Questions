# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:



        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)













        # arr1 = []
        # def dfs(Node):
        #     nonlocal arr1
        #     if not Node:
        #         arr1.append("n")
        #         return 
        #     arr1.append(Node.val)
        #     dfs(Node.left)
        #     dfs(Node.right)

        # arr2 = []
        # def dfs2(Node):
        #     nonlocal arr2
  
        #     if not Node:
        #         arr2.append("n")
        #         return 
        #     arr2.append(Node.val)
        #     dfs2(Node.left)
        #     dfs2(Node.right) 

        # dfs(p)
        # dfs2(q)
      
        # return arr1 == arr2

        
