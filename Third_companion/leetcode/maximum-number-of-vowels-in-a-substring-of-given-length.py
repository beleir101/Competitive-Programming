class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        mx = 0
        sr = {"a","e","i","o","u"}
        an = ""
        for x in range(k):
            an += s[x]
            if s[x] in sr:
                mx += 1
        i = 0
        j = k
        t = mx
        while j < len(s):
            if s[i] in sr:
                t -= 1
            if s[j] in sr:
                t += 1
            mx = max(t,mx)
            i += 1
            j += 1
        return mx