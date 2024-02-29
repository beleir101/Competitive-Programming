class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N, visited = len(nums), set()
        for i in range(N):
            if i not in visited:
                s = set()
                while True:
                    if i in s: 
                        return True
                    if i in visited: 
                        break          
                    visited.add(i)
                    s.add(i)
                    prev, i = i, (i + nums[i]) % N
                    if prev == i or (nums[i] > 0) != (nums[prev] > 0):
                        break
        return False