class Solution:
    def isToeplitzMatrix(self, matrix):
        f = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j in f:
                    if f[i-j] != matrix[i][j]:
                        return False
                else:
                    f[i-j] = matrix[i][j]
        return True
