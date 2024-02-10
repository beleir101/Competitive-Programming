class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre = []
        for i in range(len(matrix)+1):
            p = []
            for j in range(len(matrix[0])+1):
                p.append(0)
            self.pre.append(p)
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                self.pre[x+1][y+1]=self.pre[x+1][y]+self.pre[x][y+1]-self.pre[x][y]+matrix[x][y]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre[row2+1][col2+1]-self.pre[row1][col2+1]-self.pre[row2+1][col1]+self.pre[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)