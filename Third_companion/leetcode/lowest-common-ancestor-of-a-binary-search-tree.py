# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [10**10]
        def trav(x):
            
            if not x:
                return
            if(x.val < p.val and x.val > q.val) or (x.val > p.val and x.val < q.val):
                ans[0] = x
                return x
            if ((x.val == p.val) or (x.val == q.val)) and ans[0] == 10**10:
                ans[0] = x
                return x
            trav(x.left)
            trav(x.right)
        trav(root)
        return ans[0]
