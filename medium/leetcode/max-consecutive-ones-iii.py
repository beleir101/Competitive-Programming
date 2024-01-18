""" class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        zeros = deque()
        ones = 0
        mx=0
        for i in nums:
            if len(zeros)==k and i == 0:
                if k == 0:
                    mx = max(mx, ones)
                    ones = 0
                else:
                    mx = max(mx, ones+k)
                    ones -= zeros.popleft()
                    zeros.append(ones)
            elif i == 0:
                if len(zeros)==0:
                    zeros.append(ones)
                else:
                    if zeros[-1] == 0:
                        zeros.append(0)
                        continue
                    zeros.append(ones-zeros[-1])
            else:
                ones += 1
        
        mx = max(mx,ones+len(zeros))
        return mx """

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        res = -math.inf

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)

        return res