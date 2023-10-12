import sys
from collections import defaultdict
c = int(sys.stdin.readline())
games = []
for i in range(c):
    d = list(map(int,sys.stdin.readline().split()))
    games.append(d)
st = defaultdict(list)
for j in range(c):
    for x in range(c):
        if games[j][x] == 1:
            st[j+1].append(x+1)
for v in st:
    print(len(st[v]), *st[v])
