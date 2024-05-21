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
    ans = [[0]*(3) for i in range(N+1)]
    q = []
    for i in range(N):
        q.append(mp())
    ans[1] = q[0]
    for i in range(1, N):
        ans[i+1][0] = max(ans[i][1]+q[i][0], ans[i][2]+q[i][0], ans[i-1][0] + q[i][0])
        ans[i+1][1] = max(ans[i][0] + q[i][1], ans[i][2] + q[i][1], ans[i-1][1] + q[i][1])
        ans[i+1][2] = max(ans[i][0] + q[i][2], ans[i][1] + q[i][2], ans[i-1][2] + q[i][2])
    #print(ans, "ans")
    return max(ans[N])

print(chk())
