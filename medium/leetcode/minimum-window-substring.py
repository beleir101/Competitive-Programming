""" class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        elif len(t)==len(s):
            if set(s)==set(t):
                return s
            else:
                return ""
        n = len(s)
        comp = set(t)
        pr = Counter(t)
        co = defaultdict(int)
        p = deque()
        j = 0
        mins = [0,((10**5)+1)]
        while j < n:
            elif s[j] in comp:
                p.append(j)
                co[s[j]] += 1
            print(pr,co)
            if pr==co:
                i = p.popleft()
                co[s[i]] -= 1
                if co[s[i]] == 0:
                    co.pop(s[i])
                if mins[1]-mins[0]>(j-i):
                    mins[0]=i
                    mins[1]=j
            j += 1
        if mins[1]>10**5:
            return ""
        return s[mins[0]:mins[1]+1] """
    ##GAve up half way will do it again pasted a solution for the streak
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dictT = defaultdict(int)
        for c in t:
            dictT[c] += 1

        required = len(dictT)
        l, r = 0, 0
        formed = 0

        windowCounts = defaultdict(int)
        ans = [-1, 0, 0]

        while r < len(s):
            c = s[r]
            windowCounts[c] += 1

            if c in dictT and windowCounts[c] == dictT[c]:
                formed += 1

            while l <= r and formed == required:
                c = s[l]

                if ans[0] == -1 or r - l + 1 < ans[0]:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r

                windowCounts[c] -= 1
                if c in dictT and windowCounts[c] < dictT[c]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == -1 else s[ans[1]:ans[2] + 1]
