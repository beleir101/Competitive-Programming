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
    N, W = mp()
    q = []
    su = 0
    for i in range(N):
        x, y = mc()
        su += y
        q.append([x, y])

    ans = [10**9]*(su+1)
    ans[0] = 0


    for p in q:
        for i in range(su, -1, -1):
                ans[i] = min(ans[i], ans[i-p[1]]+p[0])
    #print("ans", ans)
    for i in range(su, -1, -1):
        if ans[i] <= W:
            return i


print(chk())
