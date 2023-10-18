"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.maxs = 0
    def maxDepth(self, root, leng=1):
        print(leng,self.maxs)
        if root is None:
            return 0
        if leng > self.maxs:
            self.maxs = leng
        for i in root.children:
            self.maxDepth(i,leng+1)
        return self.maxs

