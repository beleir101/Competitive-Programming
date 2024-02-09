class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        pr = [0]*N
        suf = [0]*(N+1)
        outs = ""
        for i in range(len(shifts)):
            if not shifts[i][2]:
                pr[shifts[i][0]] -= 1
                if shifts[i][1]+1 < N:
                    pr[shifts[i][1]+1] += 1
            else:
                pr[shifts[i][0]] += 1
                if shifts[i][1]+1 < N:
                    pr[shifts[i][1]+1] -= 1
        
        for x in range(N):
            suf[x]=suf[x-1]+pr[x]
        for y in range(N):
            p = ord(s[y])+suf[y]
            if p > 122:
                p -= (math.ceil((p-122)/26))*26
            elif p < 97:
                p += (math.ceil((97-p)/26))*26
            outs += chr(p)
        return outs