class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        mx = 0
        N = len(tasks)
        processorTime.sort(reverse = True)
        tasks.sort()
        i = 1
        for x in range(3, N,4):
            mx = max(mx, processorTime[x-3*i]+tasks[x])
            i += 1
        return mx