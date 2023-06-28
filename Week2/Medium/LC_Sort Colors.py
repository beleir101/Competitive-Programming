"""used merge sort to sort the list and updated values in nums since we cant return anything
    and its call by value not call by reference.
    Runtime beats 67.44%
    Memory Beats 72.64%
"""
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def MergeSort(lst):
            size = len(lst)
            if size == 1:
                return lst
            mid = size // 2

            #print(lst)
            leftHalf = MergeSort(
                lst[:mid])
            rightHalf = MergeSort(lst[
                                  mid:])
            #print(leftHalf, rightHalf)
            return Merge(leftHalf, rightHalf)

        def Merge(lst1, lst2):
            result = []

            inx1 = 0
            inx2 = 0
            while inx1 < len(lst1) and inx2 < len(lst2):
                if lst1[inx1] < lst2[inx2]:
                    result.append(lst1[inx1])
                    inx1 += 1
                else:
                    result.append(lst2[inx2])
                    inx2 += 1

            while inx1 < len(lst1):
                result.append(lst1[inx1])
                inx1 += 1
            while inx2 < len(lst2):
                result.append(lst2[inx2])
                inx2 += 1
            #print(result)
            return result
        num = MergeSort(nums)
        for i in range(len(num)):
            if num[i] != nums[i]:
                nums[i] = num[i]
nums = [0,1,0,0,1,2,1,2,2]
trial =Solution()
trial.sortColors(nums)
print(nums)