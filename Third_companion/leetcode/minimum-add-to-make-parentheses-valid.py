class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o = []
        c = []

        for x in s:
            if x == ")":
                if len(o)==0:
                    c.append(x)
                else:
                    o.pop()
            else:
                o.append(x)
        return len(o)+len(c)