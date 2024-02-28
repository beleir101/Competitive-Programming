# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, pt: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p = [True]
        def help(r,s):
            if not r and s:
                p[0] = False
                return False
            if not s and r:
                p[0] = False
                return False
            if not r:
                return True
            if r.val != s.val:
                p[0] = False
                return False
            if not help(r.right, s.right):return False
            help(r.left, s.left)
            return p[0]
        return help(pt, q)