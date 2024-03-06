class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        ans = [-1,-1]
        l, r = 0, N-1
        while l <= r:
            mid = (l+r)//2

            if nums[mid]==target:
                i,j=mid,mid
                while i>-1 and nums[i]==target:
                    i-=1
                while j<N and nums[j]==target:
                    j += 1
                return [i+1,j-1]
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return ans