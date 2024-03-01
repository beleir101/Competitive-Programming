class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        avails = [True]*N
        ans = []
        def help(t,avails,c):
            ans.append(t[:])
            if len(t) > len(nums):
                return
            for x in range(c,len(nums)):
                if avails[x]:
                    t.append(nums[x])
                    avails[x] = False
                    help(t, avails,x)
                    t.pop()
                    avails[x] = True
        help([],avails,0)
        return ans