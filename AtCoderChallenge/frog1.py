from collections import defaultdict
import random
import sys

rand = random.randint(1217, 2000)


def mp():
    return list(map(int, sys.stdin.readline().strip().split()))


def num():
    return int(sys.stdin.readline().strip())


def st():
    return sys.stdin.readline().strip()


def mc():
    return map(int, input().split())


def chk():
    N = num()
    a = mp()
    ans = [0]*(N+1)
    for i in range(1, N):

        ans[i+1] = ans[i]+abs(a[i-1] - a[i])
        if i > 1:
            ans[i+1] = min(ans[i+1], abs(a[i-2]-a[i])+ans[i-1])
    return ans[N]

print(chk())
