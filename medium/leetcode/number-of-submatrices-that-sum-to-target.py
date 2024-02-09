##pasted a solution will do it again !!
class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        pre = []
        for i in range(len(matrix)+1):
            v =[]
            for j in range(len(matrix[0])+1):
                v.append(0)
            pre.append(v)

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                pre[x+1][y+1]=pre[x][y+1]+pre[x+1][y]-pre[x][y]+matrix[x][y]
        tt = 0
        for r in range(len(matrix)):
            for s in range(r, len(matrix)):
                p = defaultdict(int)
                p[0]=1
                for c in range(len(matrix[0])):
                    y = pre[s+1][c+1]-pre[r][c+1]
                    if y-target in p:
                        tt += p[y-target]
                    p[y] += 1
        return tt