class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        duplicate = 0
        list = []
        for i in range(size):
            if nums[i] != val:
                list.append(nums[i])
                duplicate += 1
        for j in range(len(list)):
            nums[j] = list[j]
        return len(list)