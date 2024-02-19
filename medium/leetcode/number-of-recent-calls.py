
class RecentCounter:
    def __init__(self):
        self.qu = deque()
        self.ln = 0
    def ping(self, t: int) -> int:
            while self.ln>0 and t-self.qu[0] > 3000:
                self.ln -= 1
                n = self.qu.popleft()
            self.qu.append(t)
            self.ln += 1
            return self.ln


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)