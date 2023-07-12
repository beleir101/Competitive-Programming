"""
run time beats 26%
memory beats 30%
"""
class Solution:
    def numIdenticalPairs(self, nums):
        dict = {0:1, 1:1,2:3,3:6,4:10}
        def factorial(num):
            if num in dict:
                return dict[num]
            dict[num] = num + factorial(num-1)
            return dict[num]
        c = []
        in_nums = []
        sum = 0
        for i in range(len(nums)):
            if nums[i] in in_nums:
                continue
            elif nums.count(nums[i]) > 1:
                in_nums.append(nums[i])
                c.append(nums.count(nums[i]))
        print(c)
        for k in c:
            #print(k)
            sum += factorial(k-1)
        return sum



trial = Solution()
print(trial.numIdenticalPairs([4,4,2,2]))