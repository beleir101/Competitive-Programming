class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.leng = len(nums)
        self.lef = [0]*self.leng
        self.righ = [0]*self.leng
        for i in range(1,self.leng):
            self.lef[i] += self.nums[i-1] + self.lef[i-1]
        for j in range(self.leng-2,-1,-1):
            self.righ[j] = self.nums[j+1] + self.righ[j+1]
    def sumRange(self, left, right):
        return self.lef[self.leng-1]+self.nums[self.leng-1] - (self.lef[left]+self.righ[right])