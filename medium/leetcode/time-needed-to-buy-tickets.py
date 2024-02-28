class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        N = len(tickets)
        v = 0
        tt = 0
        z = 0
        while tickets[k] > 0:
            for y in range(N):
                if tickets[y]==0 and y!=k:
                    z += 1
                    continue
                tt+=1
                tickets[y]-=1
                if tickets[y]==0 and y == k:
                    return tt
                
        return tt