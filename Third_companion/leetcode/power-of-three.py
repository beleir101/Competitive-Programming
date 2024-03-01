class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        if int(n) != n:
            return False
        return self.isPowerOfThree(n/3)