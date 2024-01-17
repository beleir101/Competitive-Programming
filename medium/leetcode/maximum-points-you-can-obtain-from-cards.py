class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = [0]*(len(cardPoints)+1)
        right = [0]*(len(cardPoints)+1)
        for x in range(len(cardPoints)):
            left[x+1] = left[x]+cardPoints[x]
        r = 0
        for y in range(len(cardPoints)-1,-1,-1):
            right[r+1]= right[r]+cardPoints[y]
            r += 1
        outs = 0
        i = 1
        j = k-1
        while j > 0 and i< len(right):
            outs = max(right[i]+left[j],outs)
            i += 1
            j -= 1
        outs = max(outs,max(right[k],left[k]))
        return outs