# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sums = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        

        def dfs(Node,curr_sum):

            if not Node:
                return 0
            
            curr_sum +=Node.val

            count = 0
            if curr_sum == targetSum:
                count+=1
            
            count+= dfs(Node.left,curr_sum)
            count+= dfs(Node.right,curr_sum)

            return count

        
        if not root:
            return 0
        
        return (
            dfs(root,0) +
            self.pathSum(root.left,targetSum) +
            self.pathSum(root.right,targetSum)
        )
         
        
            
