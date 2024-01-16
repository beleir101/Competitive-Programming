""" class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p = defaultdict(int)
        j = 0
        mx = 0
        e1,e2,ec1,ec2 = -1,-1,0,0
        for i in range(len(s)):
            if e1 == -1:
                e1 = s[i]
                ec1 +=1
            elif e2==-1 and s[i]!=e1:
                e2=s[i]
                ec2 += 1
            elif s[i]!=e1 and s[i]!=e2:
                while ec1 > 0 and ec2 > 0 and j < len(s):
                    if s[j]==e1:
                        ec1 -= 1
                    elif s[j]==e2:
                        ec2 -= 1
                    j += 1
                if ec1 == 0:
                    e1 = s[i]
                    ec1 += 1
                elif ec2 == 0:
                    e2 = s[i]
                    ec2 += 1
            elif s[i]==e1:
                ec1 += 1
            elif s[i]==e2:
                ec2 += 1
            while ec1 > k and ec2>k and j < len(s):
                if s[j]==e1:
                    ec1 -= 1
                elif s[j]==e2:
                    ec2 -= 1
                j += 1
            mx = max(ec1+ec2, mx)
        return mx      
        
        I GAVE UP !!!
               """
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hasho = {}
        most_frequent = 0
        start = 0
        max_len = 0

        for end, char in enumerate(s):
            
            hasho[char] = hasho.get(char, 0) + 1 
            
            most_frequent = max(most_frequent, hasho[char])
            # (end - start + 1) --> window size 
            if (end - start + 1) - most_frequent > k:
                hasho[s[start]] -= 1
                start += 1
            
            max_len = max(max_len, end-start+1)
        
        return max_len