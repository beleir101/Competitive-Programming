class Solution:
    def simplifyPath(self, s: str) -> str:
        N = len(s)
        my_stack = []
        x = 0
        while x < N:
            j = x
            i = x
            while j < N and s[j] == ".":
                j += 1
            if j-x > 2 and (j>=N or s[j]=="/"):
                my_stack.append("."*(j-x))
                x = j
                continue
            
            elif s[x]=="/":
                x += 1
                continue
            elif j-x==2 and (j>=N or s[j]=="/"):
                if len(my_stack)==0:
                    x += 1
                    continue
                
                my_stack.pop()
                x += 1
                continue
            elif j-x == 1 and (j>=N or s[j]=="/"):
                x = j
                continue
            
            else:
                st = ""
                while i < N and s[i]!="/":
                    st += s[i]
                    i += 1
                my_stack.append(st)
                x = i
                continue
        return "/"+"/".join(my_stack)