# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        if not root.right or not root.left:
            return False
        def chk(l,r):
            if not r and l:
                return False
            if not l and r:
                return False
            if not l:
                return True
            if l.val != r.val:
                return False
            x = chk(l.left,r.right)
            y = chk(l.right, r.left)
            return x and y
        return chk(root.left, root.right)