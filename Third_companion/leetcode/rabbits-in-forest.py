class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        r = Counter(answers)
        tt = 0

        for x in r:
            group = ((r[x]-1)//(x+1))+1
            tt += group*(x+1)
        return tt