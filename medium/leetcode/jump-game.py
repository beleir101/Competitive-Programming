class Solution:
    def canJump(self, nums: List[int]) -> bool:
        d = {}
        k = set()
        def help(x,k):
            if 1 in k:
                return True
            if x in d:
                if d[x]==True:
                    k.add(1)
                return d[x]
            d[x]=False
            if x == len(nums)-1:
                d[x] = True
                k.add(1)
                return True
            if x >= len(nums):
                return False
            if not(1 in k):
                for y in range(x+nums[x],x,-1):
                    d[x] = help(y,k)
                    if d[x] or 1 in k:
                        k.add(1)
                        break
            return 1 in k
        return help(0,k)
        
