class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outs = []
        nums.sort()
        for i in range(len(nums)):

            k,j = i+1, len(nums)-1
            if i != 0 and nums[i]==nums[i-1]:
                continue
            while k < j:
                if k != i+1 and nums[k]==nums[k-1]:
                    k += 1
                    continue
                elif nums[i]+nums[k]+nums[j] == 0:
                    outs.append([nums[i],nums[k],nums[j]])
                    k += 1
                    j -= 1
                elif nums[i]+nums[k]+nums[j] < 0:
                    k+=1
                elif nums[i]+nums[k]+nums[j] > 0:
                    j -= 1
        
        return outs
