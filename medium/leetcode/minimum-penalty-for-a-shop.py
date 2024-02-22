class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        prn = [0]*(N+1)
        pry = [0]*(N+1)
        mx = [10**9,10**9]
        for x in range(N):
            if customers[x]=="N":
                prn[x+1] = prn[x]+1
                pry[x+1] = pry[x]
            else:
                prn[x+1] = prn[x]
                pry[x+1] = pry[x]+1
        for i in range(N,-1,-1):
            r = prn[i]+(pry[-1]-pry[i])
            if r <= mx[0]:
                mx = [r,i]
        return mx[1]