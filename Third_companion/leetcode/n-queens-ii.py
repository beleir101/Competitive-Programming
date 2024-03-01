class Solution:
        def __init__(self):
            self.heldcols = defaultdict(int)
            self.heldrow = defaultdict(int)
            self.helddiag = defaultdict(int)
            self.diag = defaultdict(int)
            self.ans = []
            self.curr = []
        def totalNQueens(self, n: int) -> int:
            def solver(r,c):
                if self.heldcols[c] == 0 and self.heldrow[r]==0 and self.helddiag[r-c]==0 and self.diag[c+r]==0:
                    self.heldcols[c] += 1
                    self.heldrow[r] += 1
                    self.helddiag[r-c] +=1
                    self.diag[c+r]+=1
                    return True
                return False
            def availer(r,c):
                self.heldcols[c] -= 1
                self.heldrow[r] -= 1
                self.helddiag[r-c] -=1
                self.diag[c+r] -= 1
            def runner(r):
                if r >= n:
                    self.ans.append(self.curr[:])
                    return
                for c in range(n):
                    if solver(r,c):
                        self.curr.append([r,c])
                        runner(r+1)
                        x = self.curr.pop()
                        availer(x[0],x[1])
                return
            runner(0)
            return len(self.ans)