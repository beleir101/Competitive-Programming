class Solution:
    def productExceptSelf(self, nums):
        pro = [1,0]
        outy = []
        for i in nums:
            if i == 0:
                pro[1] += 1
                continue
            pro[0] *= i
        if pro[1] == 0:
            for j in nums:
                outy.append(int(pro[0]/j))
        else:
            for j in nums:
                if j == 0 and pro[1] == 1:
                    outy.append(int(pro[0]))
                else:
                    outy.append(0)
        return outy