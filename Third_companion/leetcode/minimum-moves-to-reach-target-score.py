class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target > 0:
            if maxDoubles == 0:
                return ans + target-1
            elif target % 2:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
            ans += 1
        return ans-1