#thought using heaps will make it faster and menory efficient but I was wrong I guess :(
#Run time beats 14%
#Memory Beast 77%
import heapq
class Solution:
    def targetIndices(self, nums, target):
        heapq.heapify(nums)
        sorted = []
        indexs = []
        for i in range(len(nums)):
            sorted.append(heapq.heappop(nums))
        for k in range(len(sorted)):
            if sorted[k] == target:
                indexs.append(k)
            elif sorted[k] > target:
                break
        return indexs
trial = Solution()
trial.targetIndices(nums = [1,2,5,2,3], target = 2)