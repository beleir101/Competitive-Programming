class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lon = ""
        strs.sort(key = lambda x:len(x))
        for i in range(len(strs[0])):
            if strs[0][i] != strs[1][i] or strs[1][i] != strs[2][i] or strs[0][i] != strs[2][i]:
                return lon
            lon += strs[0][i]
        return lon