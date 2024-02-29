# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        

        k = deque()
        k.append(root)
        realmx = 0
        while len(k)>0:
            kr = k.popleft()
            if not kr:
                continue
            k.append(kr.left)
            k.append(kr.right)
            p = deque()
            p.append(kr)
            element = kr.val
            mx = 0
            while len(p)>0:
                newpoped = p.popleft()
                if not newpoped:
                    continue
                p.append(newpoped.left)
                p.append(newpoped.right)
                mx = max(mx,abs(element-newpoped.val))
            realmx = max(realmx,mx)
        return realmx