from collections import deque
class Solution:
    def evalRPN(self, tokens):
        stacked = deque()
        for i in tokens:
            if i != "+" and i != "-" and i != "*" and i != "/":
                stacked.append(int(i))
            else:
                b = stacked.pop()
                a = stacked.pop()
                if i == "+":
                    stacked.append(a+b)
                elif i == "-":
                    stacked.append(a-b)
                elif i == "*":
                    stacked.append(a*b)
                elif i == "/":
                    stacked.append(int(a/b))
        return stacked.pop()