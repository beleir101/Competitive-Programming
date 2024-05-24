import threading
from collections import defaultdict
import random
import sys
from sys import stdin,stdout,setrecursionlimit
rand = random.randint(1217, 2000)

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def main():

    def mp():
        return list(map(int, sys.stdin.readline().strip().split()))

    def num():
        return int(sys.stdin.readline().strip())

    def st():
        return sys.stdin.readline().strip()

    def mc():
        return map(int, input().split())

    def chk():
        N, M = mc()
        e = defaultdict(list)
        dp = [-1] * (N + 1)
        for i in range(M):
            t = mp()
            e[t[0]].append(t[1])

        def trav(i):
            if dp[i] > -1:
                return dp[i]
            bst = 0
            for x in e[i]:
                bst = max(bst, trav(x) + 1)
            dp[i] = bst

            return dp[i]

        for x in range(1, N + 1):
            trav(x)

        return max(dp)

    print(chk())


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()





