class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        if r==1:
            if target in matrix[0]:
                return True
            return False
        c = len(matrix[0])
        t = -2
        for x in range(r):
            if matrix[x][0] > target:
                t = x-1
                break
            elif matrix[x][0]==target:
                return True
        if t==-2:
            return target in matrix[r-1]
        if  t < 0:
            return False
        if target in matrix[t]:
            return True
        return False