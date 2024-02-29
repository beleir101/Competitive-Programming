class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        m = (10**9)+7
       
        d = []
        arr = [(-3*(10**4))-1]+arr+[(-3*(10**4))-1]
        n = len(arr)
        ans = 0
        for i in range(n):
            if len(d)==0:
                d.append(i)
            if len(d)>0:
                rv = d.pop()
                if arr[rv]>arr[i]:
                    while len(d)>0 and arr[rv]>arr[i]:
                        ans += (i-rv)*arr[rv]*(rv-d[-1])
                        rv = d.pop()
                    d.append(rv)
                    if rv != i:
                        d.append(i)
                else:
                    d.append(rv)
                    if i != rv:
                        d.append(i)
        return ans%m
                
