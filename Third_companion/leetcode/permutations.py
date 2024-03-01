class Solution:
    def permute(self, nums):
        def produce(num, starter, puter,outed):
            if len(puter) == len(num):
                outed.append(puter[:])
                puter.pop()
                return
            for i in range(len(nums)):
                if puter.count(nums[i]) == 0:
                    puter.append(nums[i])
                    produce(nums, starter + 1, puter, outed)
            if puter != []:
                puter.pop()
            elif puter == []:
                return outed
        return produce(nums,0,[],[])