#runtime beats 76.3%, memory beats 95%
class Solution:
    def sortSentence(self, s: str) -> str:
        words = []
        original = []
        words += s.split()
        for i in range(len(words)):
            original.append(" ")
        for k in words:
            size = len(k)
            #print(k[size-1])
            p = int(k[size-1]) - 1
            original[p] = k
        statement = ""
        for j in original:
            size = len(j)
            statement += j[:size-1] + " "
        return statement[:len(statement)-1]




trial = Solution()
print(trial.sortSentence("Myself2 Me1 I4 and3"))