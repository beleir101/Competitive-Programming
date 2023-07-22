
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        print(piles)
        appendy = []
        sum = 0
        j = -1
        size = len(piles)-2
        while size > j:
            sum += piles[size]
            size -= 2
            j += 1
        return sum
