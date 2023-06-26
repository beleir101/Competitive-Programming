#leetCode
#run time beats 96.6% memory beats 82%
class Solution:
    def fizzBuzz(self, n: int):
        out = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5 ==0:
                    out.append("FizzBuzz")
                else:
                    out.append("Fizz")
            elif i % 5 == 0:
                out.append("Buzz")
            else:
                out.append(str(i))
        return out
