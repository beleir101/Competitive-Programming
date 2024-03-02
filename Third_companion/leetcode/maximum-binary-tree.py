# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(x):
            if len(x)==0:
                return
            mv = max(x)
            i = x.index(mv)
            m = TreeNode(x[i])
            m.left = build(x[:i])
            m.right = build(x[i+1:])
            return m
        return build(nums)