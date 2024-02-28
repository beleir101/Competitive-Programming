# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def help(a, b):
            t = None
            if a and b:
                t = TreeNode(a.val+b.val)
                t.left = help(a.left, b.left)
                t.right = help(a.right, b.right)
            elif a:
                t = TreeNode(a.val)
                t.left = help(a.left, b)
                t.right = help(a.right, b)
            elif b:
                t = TreeNode(b.val)
                t.left = help(a, b.left)
                t.right = help(a, b.right)
            return t
        return help(root1, root2)