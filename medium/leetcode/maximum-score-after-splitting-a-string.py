class Solution:
    def maxScore(self, s: str) -> int:
        z = s.count("0")
        o = s.count("1")
        l = 0
        lr = 0
        r = o
        rr = len(s)
        score = 0
        for i in s:
            if i == "0":
                l += 1
            else:
                r -= 1
            lr += 1
            rr -= 1
            if lr > 0 and rr > 0:
                score = max(score,l+r)
        return score