class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def help(l,r):
            if l >  r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            lp = nums[l] - help(l+1, r)
            rp = nums[r] - help(l, r-1)
            dp[(l,r)] = max(lp, rp)
            return dp[(l, r)]
        return help(0, len(nums)-1) > -1
