class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        d = defaultdict(int)

        def pasc(n):
            if n == 0:
                d[0] = [1]
                return [1]
            if n in d:
                return d[n]
            r = [0]*(n+1)
            for x in range(n+1):
                if x == 0:
                    r[x] = pasc(n-1)[0]
                elif x==n:
                    r[x]=pasc(n-1)[n-1]
                else:
                    r[x]=pasc(n-1)[x-1]+pasc(n-1)[x]
            d[n]=r
            return r

        return pasc(rowIndex)