# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        # print(root.val)
        if not root:
            return ans
        

        queue = deque([root])
        
        while queue:
            vals = []

            size = len(queue)
            for _ in range(size):

                node = queue.popleft()
                vals.append(node.val)
                if node.left:
                    queue.append(node.left)  
                if node.right:
                    queue.append(node.right)
                  
            
            ans.append(vals)
                
        return ans
                
