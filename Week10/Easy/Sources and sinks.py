import sys
c = int(sys.stdin.readline())

games = []
for i in range(c):
    d = list(map(int,sys.stdin.readline().split()))
    games.append(d)
sources = list(range(1,c+1))
sinks = []
for j in range(c):
    No = True
    for x in range(c):
        if games[j][x] == 1:
            No = False
            sources.remove(x+1)
    if No:
        sinks.append(j+1)
print(len(sources), end = " ")
for i in sources:
    print(i, end = " ")
print()
print(len(sinks), end = " ")
for j in sinks:
    print(j, end=" ")

