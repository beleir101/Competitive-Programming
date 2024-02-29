# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(x,outs):
            if not x:
                return 
            
            else:
                if low <= x.val <= high:
                    outs[0] += x.val
                dfs(x.left,outs)
                dfs(x.right,outs)
                return outs[0]
        
        return dfs(root,[0])