#runtime beats 46%
#memory beats 68%
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        numbers_lower = 0
        outed = []
        for i in nums:
            for k in range(len(nums)):
                if i > nums[k]:
                    numbers_lower += 1
            outed.append(numbers_lower)
            numbers_lower = 0
        return outed
trial = Solution()
print(trial.smallerNumbersThanCurrent([5,0,10,0,10,6]))