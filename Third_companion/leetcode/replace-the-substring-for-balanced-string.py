class Solution:
    def balancedString(self, s: str) -> int:
        N = len(s)
        p = defaultdict(int)
        r = Counter(s)
        ans = float('inf')
        i,j = 0,0
        br = False
        for x in r:
            if r[x] != N//4:
                br = True
                break
        if br:
            while i <= j and j < N:
                r[s[j]] -= 1
                while max(r.values()) <= N//4 and i <= j:
                    ans = min(j-i+1, ans)
                    r[s[i]] += 1
                    i += 1
                j += 1
        if ans == float('inf'):
            return 0
        return ans