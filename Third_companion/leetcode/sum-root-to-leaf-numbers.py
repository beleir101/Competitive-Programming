# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ans = [0]
        def trav(x, upto):
            if not x.left and not x.right:
                ans[0] += int("".join(upto))
                return
            if not x.left:
                trav(x.right,upto+[str(x.right.val)])
                return
            if not x.right:
                trav(x.left,upto+[str(x.left.val)])
                return
            trav(x.left,upto+[str(x.left.val)])
            trav(x.right,upto+[str(x.right.val)])
        trav(root, [str(root.val)])
        return ans[0]


            