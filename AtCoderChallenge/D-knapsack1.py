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
    N, W = mc()
    brd = [[0]*(W+1) for i in range(N+1)]
    q = []
    for i in range(N):
        q.append(mp())
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j >= q[i-1][0]:
                brd[i][j] = max(q[i-1][1] + brd[i-1][j-q[i-1][0]], brd[i-1][j])
            else:
                brd[i][j] = brd[i-1][j]
    #print("brd", brd)
    return brd[N][W]


print(chk())
