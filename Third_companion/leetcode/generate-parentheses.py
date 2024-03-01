class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def builder(op,cl, s,v):
            if op == cl == n:
                v.add(s)
                return v
            if op < n:
                builder(op+1,cl,s+"(",v)
            if cl<op:
                builder(op, cl+1,s+")",v)
            return v
        
        return builder(0,0,"",set())
