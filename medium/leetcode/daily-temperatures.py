class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mx = [0,0]
        N = len(temperatures)
        v = []
        for i in range(N-1,-1,-1):
            if mx[0]>temperatures[i]:
                br = True
                for j in range(i+1,mx[1]):

                    if temperatures[i]==temperatures[j]:
                        v.append(v[N-j-1]+j-i)
                        br = False
                        break
                    if temperatures[i]<temperatures[j]:
                        v.append(j-i)
                        br = False
                        break
                if br:
                    v.append(mx[1]-i)
            else:
                v.append(0)
                mx[0], mx[1]=temperatures[i], i
        return v[::-1]