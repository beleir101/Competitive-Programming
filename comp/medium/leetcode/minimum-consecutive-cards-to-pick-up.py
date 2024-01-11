class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        d = defaultdict(list)
        for i,v in enumerate(cards):
            if v not in d:
                d[v] = [-1,10**6]
            if d[v][0] != -1:
                d[v][1] = min(d[v][1],i-d[v][0]+1)
            d[v][0] = i
        ms = 10**6
        for x in d:
            ms = min(d[x][1],ms)
        if ms == 10**6:
            return -1
        return ms