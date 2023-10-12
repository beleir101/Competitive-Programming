class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[1].count(edges[0][0])>0:
            return edges[0][0]
        return edges[0][1]