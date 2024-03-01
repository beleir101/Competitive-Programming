class Solution:
    def combinationSum(self, candidates, target):
        def helper(target,main,avails,now):
            if target < 0:
                return
            if target == 0:
                main[tuple(sorted(now))] = sorted(now)
            for x in avails:
                now.append(x)
                helper(target - x,main,avails,now)
                now.pop()
        np = []
        ds = {}
        helper(target,ds,candidates,np)
        return list(ds.values())