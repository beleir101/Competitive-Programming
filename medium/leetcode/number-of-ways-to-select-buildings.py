class Solution:
    def numberOfWays(self, s: str) -> int:
        N = len(s)
        pro = [0]*(N+1)
        prz = [0]*(N+1)
        for i in range(N):
            if s[i] == "0":
                pro[i+1] = pro[i] + 1
            else:
                pro[i+1] = pro[i]
            if s[i] == "1":
                prz[i+1] = prz[i] + 1
            else:
                prz[i+1] = prz[i]
        mx = 0
        for x in range(N):
            if s[x]=="1":
                mx += pro[x]*(pro[N]-pro[x])
            elif s[x]=="0":
                mx += prz[x]*(prz[N]-prz[x])
        return mx
