class Solution:
    def hIndex(self, nums: List[int]) -> int:
        N = len(nums)
        i,j = 0,N-1
        while i<j:
            if i+1==j:
                p,r = 0,0
                if N-j <= nums[j]:
                    p = min(N-j,nums[j])
                if N-i <=nums[i]:
                    r = min(N-i,nums[i])
                return max(p,r)
            mid = (i+j)//2
            if nums[mid] <= N-mid:
                i = mid
            else:
                j=mid
        return min(nums[i], N)