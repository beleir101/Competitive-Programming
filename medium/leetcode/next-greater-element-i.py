class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        nums2.append(10**5)
        st = []
        i = 1
        for x in nums2:
            if st == []:
                st.append(x)
            while st and x>st[-1]:
                d[st.pop()] = x
            st.append(x)
        ans = []
        for x in nums1:
            if d[x]==10**5:
                ans.append(-1)
            else:
                ans.append(d[x])
        return ans
