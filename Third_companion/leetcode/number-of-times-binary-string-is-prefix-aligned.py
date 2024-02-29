""" class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        flipped = set()
        zeroes = set(flips)
        ans = 0
        for x in range(len(flips)):
            flipped.add(flips[x])
            br = True
            for y in range(1,x+1):
                if y not in flipped:
                    br = False
                    break
            if br:
                for j in range(x+2,len(flips)+1):
                    if j in flipped:
                        br = False
                        break
            if br:
                ans += 1
        return ans 
        
        Time limit made me check yt
        """
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        tot = 0
        cnt = 0
        for i, f in enumerate(flips):
            tot += f
            if tot == (i+1)*(i+2)//2:
                cnt += 1
        return cnt
