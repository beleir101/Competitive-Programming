"""
This one was also tough I gave up after 52 minutes checked a solution and tried to understand it.
"""

class Solution:
    def rearrangeArray(self, nums):
        nums.sort()
        if len(nums) == 3:
            nums[1], nums[0] = nums[0], nums[1]
            return nums
        for i in range(1, len(nums) - 1):
            if nums[i] - nums[i - 1] == nums[i + 1] - nums[i]:
                if i != len(nums) - 2:
                    nums[i + 1], nums[i + 2] = nums[i + 2], nums[i + 1]
                if i == len(nums) - 2:
                    nums[i + 1], nums[0] = nums[0], nums[i + 1]
        return nums



trial = Solution()
#[1,2,3,4,5,7]
print(trial.rearrangeArray([1,3,2,4,5,7]))



