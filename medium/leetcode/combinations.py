class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []

        def help(t,v):
            v.append(t)
            if len(v)==k:
                out.append(v.copy())
                
                return
            for x in range(t+1, n+1):
                help(x,v)
                v.pop()
        for x in range(1, n+1):
            help(x,[])
        return out