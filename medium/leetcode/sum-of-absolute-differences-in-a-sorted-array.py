class Solution:
    def getSumAbsoluteDifferences(self, nums):
        x = 1
        v = sum(nums)
        kn = -len(nums)
        outy = []
        for i in range(len(nums)):
            r = kn*nums[i]
            jn = v + r
            outy.append(jn)
            v -= 2*nums[i]
            kn += 2
        return outy