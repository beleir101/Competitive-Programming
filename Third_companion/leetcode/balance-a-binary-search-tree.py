# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        s = []
        def inorder(x):
            if not x:return
            inorder(x.left)
            s.append(x.val)
            inorder(x.right)
        def balance(ns):
            if len(ns)==0:
                return
            N = len(ns)//2
            m = TreeNode(ns[N])
            m.right = balance(ns[N+1:])
            m.left = balance(ns[:N])
            return m
        inorder(root)
        return balance(s)
