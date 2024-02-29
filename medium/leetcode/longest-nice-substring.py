class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        vr = [""]
        def calc(p):
            N = len(p)
            t = set(list(p.strip("")))
            for i in range(N):
                if p[i].swapcase() not in t:
                    td = calc(p[:i])
                    tv = calc(p[i+1:])     
                    if len(tv) > len(td):
                        vr[0] = tv
                    elif len(td)>len(vr[0]):
                        vr[0] = td
                    return vr[0]
            if len(p) > len(vr[0]):
                vr[0] = p
            return vr[0]
        calc(s)
        return vr[0]