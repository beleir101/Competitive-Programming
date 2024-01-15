class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        l = defaultdict(int)
        r = defaultdict(int)
        for i in range(len(s1)):
            l[s1[i]] += 1
            r[s2[i]] += 1
        i,j = 0,len(s1)
        while j < len(s2):
            if l == r:
                return True
            r[s2[i]] -= 1
            if r[s2[i]] < 1:
                r.pop(s2[i])
            r[s2[j]] += 1
            i += 1
            j += 1
        if l == r:
            return True
        return False