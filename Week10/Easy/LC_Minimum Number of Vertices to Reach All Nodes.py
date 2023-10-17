from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        vertices = set()
        for i in range(n):
            vertices.add(i)
        for j in edges:
            if j[1] in vertices:
                vertices.remove(j[1])
        return list(vertices)