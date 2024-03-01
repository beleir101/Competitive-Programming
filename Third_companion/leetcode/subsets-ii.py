class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        avails = [True]*N
        ans = set()
        def help(t,avails,c):
            ans.add(tuple(t[:]))
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