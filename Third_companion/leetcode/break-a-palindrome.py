class Solution:
    def breakPalindrome(self, a: str) -> str:
        p = list(a)
        N = len(a)
        if N == 1:return ""
        for x in range(N):
            if p[x] != "a":
                v = p[x]
                p[x] = "a"
                if p != p[::-1]:
                    return "".join(p)
                p[x] = v
        p[-1]="b"
        return "".join(p)