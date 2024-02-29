class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = defaultdict(int)

        i,j = 0,0
        s=0
        curr = 0
        while j<len(nums):
            if nums[j] in d and d[nums[j]] >= i:
                while i <= d[nums[j]]:
                    curr -= nums[i]
                    i += 1
                s = max(s, curr)
            curr += nums[j]
            d[nums[j]] = j
            s = max(s, curr)
            j += 1
        s = max(s, curr)
        return s