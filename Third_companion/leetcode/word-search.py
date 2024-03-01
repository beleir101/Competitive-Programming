class Solution:
    def __init__(self):
        self.chk =[]
        self.bool = False
    def exist(self, board, word):
        def helper(ptx,pty,visited,limx,limy,br,wr):
            if len(self.chk) >= len(wr):
                self.bool = True
                return True
            if ptx >= limx or pty<0 or ptx<0 or pty>=limy:
                return
            if (ptx,pty) in visited:
                return
            if br[ptx][pty] != wr[len(self.chk)]:
                return
            self.chk.append(br[ptx][pty])
            visited.add((ptx,pty))
            helper(ptx, pty+1, visited, limx, limy, br, wr)
            helper(ptx+1, pty, visited, limx, limy, br, wr)
            helper(ptx-1, pty, visited, limx, limy, br, wr)
            helper(ptx, pty-1, visited, limx, limy, br, wr)
            self.chk.pop()
            visited.discard((ptx,pty))
        for i in range(len(board)):
            if self.bool:
                break
            for x in range(len(board[0])):
                visit = set()
                p = helper(i,x,visit,len(board),len(board[0]),board,word)
                if self.bool:
                    break
        return self.bool