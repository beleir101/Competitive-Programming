class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        d = Counter(nums)
        p = 0
        s = 0
        x = 1
        i = 0
        while  s <n:
            if x in d:
                s += x*d[x]
                i += d[x]
            if i<len(nums) and x>nums[i]:
                s += nums[i]
                i += 1
            elif s < x:
                p +=1
                s += x
            x = s+1
        return p