"""
I gave Up after 32 minutes I was getting TLE error messages on test case 169 So I checked the solution
"""
from collections import deque

"""
My Solution wit TLE error
class Solution:
    def findOriginalArray(self, changed):
        size = len(changed)
        if size % 2 == 1:
            return []
        changed.sort()
        checker = []
        for j in changed:
            checker.append([j,0])
        original = []
        print(checker)
        for x in range(size-1,-1,-1):
            if checker[x][1] == 1:
                continue
            else:
                if changed.count(checker[x][0]/2) < 1:
                    return []
            c = [checker[x][0] // 2, 0]
            p = checker.index(c)
            checker[p] = [checker[x][0] // 2, 1]
            original.append(checker[p][0])
        return original

trial = Solution()
print(trial.findOriginalArray([1,3,4,2,6,8]))
"""
class Solution:
    def findOriginalArray(self, changed):
        changed.sort()
        stk,res=deque([]),[]
        for i in changed:
            print(stk,res)
            if stk and stk[0]*2==i:
                b=stk.popleft()
                res.append(b)
            else:
                stk.append(i)
        return res if not stk else []
trial = Solution()
print(trial.findOriginalArray([1,3,4,2,6,8]))