""" # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(list)
        dep = [0]
        def getdepth(x,l):
            if not x:
                return
            dep[0] = max(dep[0],l)
            getdepth(x.left, l+1)
            getdepth(x.right, l+1)
        def trav(x,l):
            if not x or l >a dep[0]:
                return
            if not x.right:
                x.right= TreeNode(-1)
            if not x.left:
                x.left = TreeNode(-1)
            d[l].append(x.val)
            trav(x.left, l+1)
            trav(x.right, l+1)
        getdepth(root,0)
        trav(root, 0)
        ans = [0]
        for x in d:
            i,j = 0,(2**x)-1
            while d[x][i] == -1:
                i += 1
            while d[x][j] == -1:
                j -= 1
            ans[0] = max(ans[0], j-i+1)
        return ans[0]   MEMORY LIMIT EXEEDED"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        lvls = []

        def helper(node, lvl, num):
            if not node:
                return

            if len(lvls) == lvl:
                lvls.append([float('+inf'), 0])

            lvls[lvl][0] = min(lvls[lvl][0], num)
            lvls[lvl][1] = max(lvls[lvl][1], num)

            helper(node.left, lvl + 1, num * 2)
            helper(node.right, lvl + 1, num * 2 + 1)

        helper(root, 0, 0)

        return max(lvl[1] - lvl[0] + 1 for lvl in lvls)