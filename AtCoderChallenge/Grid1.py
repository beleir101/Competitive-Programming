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
    N, m = mc()
    q = []
    for i in range(N):
        q.append(st())
    ans = [[0]*m for i in range(N)]

    for i in range(m-2, -1, -1):
        if q[N-1][i] == "#":
            break
        ans[N-1][i] = 1
    for j in range(N-2, -1, -1):
        if q[j][m-1] == "#":
            break
        ans[j][m-1] = 1

    for i in range(N-2, -1, -1):
        for j in range(m-2, -1, -1):
            if q[i][j] != "#":
                ans[i][j] = ans[i+1][j] + ans[i][j+1]

    return ans[0][0] % (10**9 + 7)


print(chk())
