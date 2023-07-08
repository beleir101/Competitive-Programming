class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(' : ')', '{' : '}', '[' : ']'}
        size = len(s)
        opening = []
        i = 0
        if size % 2 ==1:
            return False
        while i < size:
            if s[i] in dic:
                opening.append(s[i])
                i += 1
            else:
                if i == 0 or opening == []:
                    return False
                elif dic[opening.pop()] != s[i]:
                    return False
                else:
                    i += 1
        return opening == []