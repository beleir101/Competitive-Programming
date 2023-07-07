"""
Shittest Code took me 49 minutes I should study an easier way
runtime 16.64%
memory beats 27.83%
"""
from heapq import *
class Solution:
    def merge(self, intervals):
        intervalism = []
        interval = []
        for i in intervals:
            heappush(intervalism,i)
        while intervalism:
            interval.append(heappop(intervalism))
        #print(interval)
        def merger(inter1, inter2):
            merged = []
            if inter1[1] >= inter2[0]:
                c = inter2[1]
                if inter1[1] > inter2[1]:
                    c = inter1[1]
                merged = [inter1[0], c]
            return [inter1,merged]
        if len(interval) == 1:
            return interval
        real = []
        i = 0
        print(interval)
        while i < len(interval)-1:
            #print(i)
            merged = [interval[i], interval[i]]
            while len(merged[1]) != 0 and i < len(interval) - 1:
                merged = (merger(merged[1], interval[i + 1]))
                i += 1
            if merged[1]:
                real.append(merged[1])
            else:
                real.append(merged[0])
        x = len(real)-1
        y = len(interval) - 1
        if interval[y][1] not in range(0,real[x][1] + 1):
            real.append(interval[y])
        return real
trial = Solution()
print(trial.merge([[4,5],[1,4],[0,1]]))