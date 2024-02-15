class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s) 

        skipped = False
        s = 0 
        for x in d:
            if not d[x]%2:
                s += d[x]
            else:
                s += d[x]-1
                skipped = True
        if skipped:
            return s + 1
        return s