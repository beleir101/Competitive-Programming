class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = set()
        def trav(x,ta,s):
            if len(ta)==k:
                if s == n: 
                    ans.add(tuple(ta))
                return
            if s > n:
                return
            for y in range(x+1, 10):
                trav(y,ta+[y],s+y)
        trav(0,[],0)
        return ans