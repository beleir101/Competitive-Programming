"""
took me less thank 5 min
i dont even know why this is tagged medium it was super easy
runtime beats   67.5%
memory beats    98.71%
"""
class Solution:
    def kthLargestNumber(self, nums, k):
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        nums.sort()
        nums.reverse()
        return str(nums[k-1])


tiral = Solution()
print(tiral.kthLargestNumber(["3","6","7","10"], 4))