class Solution:
    def isValid(self, s: str) -> bool:
        p = []
        d = {")":"(",
            "}":"{",
            "]":"["}
        
        for x in s:
            if x in d:
                if len(p)==0:
                    return False
                if p.pop() != d[x]:
                    return False
            else:
                p.append(x)
        if len(p)==0:
            return True
        return False
