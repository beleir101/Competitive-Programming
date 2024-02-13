class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pr = [0]*(n+2)
        for x in bookings:
            pr[x[0]] += x[2]
            pr[x[1]+1] -= x[2]
        for x in range(n):
            pr[x+1] += pr[x]
        return pr[1:n+1]