# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        dr = []
        def trav(x):
            if not x:
                return
            dr.append(x.val)
            trav(x.right)
            trav(x.left)
        dv = set(dr)
        trav(root)
        return sorted(dr)[k-1]
