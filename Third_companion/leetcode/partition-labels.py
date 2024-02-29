class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d =  {}
        N = len(s)
        for x in range(N):
            if s[x] not in d:
                d[s[x]]=[x,x]
            d[s[x]][1] = max(d[s[x]][1], x)
        v = sorted(d, key=lambda x:d[x])
        out = []
        i = 0
        while i < len(d):
            mn,mx = d[v[i]][0], d[v[i]][1]
            j = i+1
            while j<len(d) and d[v[j]][0] < mx:
                mx = max(mx, d[v[j]][1])
                j += 1
            out.append(mx-mn+1)
            i = j
        return out
