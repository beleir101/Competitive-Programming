# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, num: List[int]) -> Optional[TreeNode]:
        def help(nums):
            N = len(nums)
            if not N:
                return
            if N == 1:
                return TreeNode(nums[0])
            x = N//2
            p = TreeNode(nums[x])
            p.right = help(nums[x+1:])
            p.left = help(nums[:x])
            return p
        return help(num)