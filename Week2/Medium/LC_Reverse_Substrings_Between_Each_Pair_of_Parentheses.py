"""what in the hell I dont even know how to do this.
Shit code done after 40 minutes will check better solutions later
runtime beats 5%
memory beats 5 %
"""
class Solution:
    def reverseParentheses(self, s):
        def sorted_returner(sub):
            stacked = Stack()
            returned = ""
            for i in sub:
                if i != "(" and i != ")":
                    stacked.push(i)
            while not stacked.is_empty():
                returned += stacked.pop()
            #print(returned)
            return returned
        STATE = False
        sorted = ""
        gonna_be_sorted = ""
        gonna = ""
        #print(s, len(s))
        gn = 0
        #print(len(s))
        while gn < len(s) and s[gn] != ")":
            #print(gn,len(s), gn < len(s))
            sorted += s[gn]
            STATE = True
            gn += 1
        gn -= 1
        if gn + 1 == len(s):
            STATE = False
        if STATE:
            while gn >= -1 and s[gn] != "(":
                gonna_be_sorted += s[gn]
                STATE = True
                gn -= 1
            g = len(gonna_be_sorted)
            for kn in range(g-1,-1,-1):
                gonna += gonna_be_sorted[kn]
            #print(gonna)
            #print(sorted)
            #print(sorted[:len(sorted) - g-1],"dd", )
            sorted = sorted[:len(sorted) - g-1] + sorted_returner(gonna) + s[len(sorted)+1:]
            return (self.reverseParentheses(sorted))
        else:
            return s
class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    def push(self, element):
        self.stack.append(element)
        self.size += 1
    def pop(self):
        self.size -= 1
        return self.stack.pop()
    def is_empty(self):
       return self.size == 0
trial = Solution()
print(trial.reverseParentheses("co(de(fight)s)"))
