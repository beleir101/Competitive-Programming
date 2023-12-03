class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lon = ""
        strs.sort(key = lambda x:len(x))
        for i in range(len(strs[0])):
            for x in strs:
                if x[i] != strs[0][i]
                    return lon
            lon += strs[0][i]
        return lon