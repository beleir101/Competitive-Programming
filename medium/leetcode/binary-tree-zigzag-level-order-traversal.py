# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        if not root.left and not root.right:
            return [[root.val]]
        d = defaultdict(list)
        ans = []
        def trav(r,n):
            if not r:return
            d[n].append(r.val)
            trav(r.left,n+1)
            trav(r.right,n+1)
        trav(root,0)
        for x in d:
            if x%2:
                ans.append(d[x][::-1])
            else:
                ans.append(d[x])
        return ans