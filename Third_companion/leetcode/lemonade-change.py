class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d ={5:0,10:0, 20:0}
        def can(x):
            if x >= 20:
                p = x//20
                if p < d[20]:
                    x -= p * 20 
                    d[20] -= p
                else:
                    x -= d[20]*20
                    d [20] = 0
            if x >= 10:
                p = x//10
                if p < d[10]:
                    x -= p*10 
                    d[10] -= p
                else:
                    x -= d[10]*10
                    d [10] = 0
            if x >= 5:
                p = x//5
                if p < d[5]:
                    x -= p*5
                    d[5] -= p
                else:
                    x -= d[5]*5
                    d[5] = 0
            return x == 0
        for x in bills:
            if x == 5:
                d[5] += 1
            else:
                if not(can(x-5)):
                    return False
                else:
                    d[x] += 1
        return True