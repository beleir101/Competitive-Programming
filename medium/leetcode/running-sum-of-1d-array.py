class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lf = [0]*(len(nums)+1)


        for i in range(len(nums)):
            lf[i+1] = lf[i]+nums[i]
        return lf[1:]