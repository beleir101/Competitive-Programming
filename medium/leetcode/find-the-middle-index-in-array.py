class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        lf = [0]*(len(nums)+1)
        rt = [0]*(len(nums)+1)

        for i in range(len(nums)):
            lf[i+1] = lf[i]+nums[i]
        y = 0
        for x in range(len(nums)-1,-1,-1):
            rt[y+1] = rt[y]+nums[x]
            y += 1
        for z in range(len(lf)-1):

            if lf[z]==rt[len(nums)-1-z]:
                return z
        return -1