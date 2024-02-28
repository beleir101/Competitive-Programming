# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        p = {}
        if root is None:
            return []
        if root.right is None and root.left is None:
            return [root.val]
        def helper(ri):
            if ri is None:
                return
            if ri.val in p:                
                p[ri.val] += 1
            else:
                p[ri.val] = 1
            helper(ri.right)
            helper(ri.left)

        helper(root)
        outs = []
        d = []
        for i in p:
            outs.append([i,p[i]])
        outs.sort(key=lambda x:x[1],reverse = True)
        j = outs[0][1]
        for x in outs:
            if x[1] != j:
                break
            d.append(x[0])
        return d