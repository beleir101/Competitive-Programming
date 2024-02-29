class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        p = []
        mx = [0]
        def indexer(r,i):
            an = ""
            v = ""
            y = 0
            while r[y].isdigit():
                v += r[y]
                y += 1
            x = y
            while x < len(r):
                if r[x].isdigit():
                    p = indexer(r[x:],x)
                    an += p[0]
                    x = p[1]
                elif r[x] == "]":
                    return [an*int(v),x+i]
                elif r[x]!="[":
                    an += r[x]
                x += 1
        i = 0
        while i < len(s):
            if s[i].isdigit():
                p = indexer(s[i:],i)
                ans.append(p[0])
                i = p[1]
            else:
                ans.append(s[i])
            i += 1
        return "".join(ans)
            

