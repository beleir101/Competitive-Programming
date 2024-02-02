class Solution:
    def minimumSteps(self, s: str) -> int:
        moves = 0
        kt = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "1":
                if len(s)-kt != i + 1:
                    moves += len(s[i+1:len(s)-kt])
                kt += 1
        return moves