class Solution:
    def fib(self, n: int) -> int:
        my_dictionary = {0 : 0, 1 : 1}
        def real_climb(stairs):
            if stairs in my_dictionary.keys():
                return my_dictionary[stairs]
            else:
                my_dictionary[stairs] = real_climb(stairs - 1) + real_climb(stairs - 2)
                return my_dictionary[stairs]
        return real_climb(n)