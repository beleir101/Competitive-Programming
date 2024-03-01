class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def trav(x,i):
            if x==1:
                return 0
            if i%2 == 1:
                if trav(x-1, math.ceil(i/2)) == 1:
                    return 1
                else:
                    return 0
            else:
                if trav(x-1, math.ceil(i/2)) == 1:
                    return 0
                else:
                    return 1
        return trav(n,k)