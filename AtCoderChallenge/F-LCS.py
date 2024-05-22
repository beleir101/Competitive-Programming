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
    s= st()
    t = st()
    N = len(s)
    M = len(t)
    brd = [[0] * (M+1) for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if s[i-1] == t[j-1]:
                brd[i][j] = brd[i-1][j-1]+1
            else:
                brd[i][j] = max(brd[i-1][j], brd[i][j-1])

    #print("brd", brd)
    out = []
    j = M
    i = N
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            out.append(s[i-1])
            i -= 1
            j -= 1
        elif brd[i][j-1] > brd[i-1][j]:
            j -= 1
        else:
            i -= 1

    return "".join(out[::-1])
print(chk())

