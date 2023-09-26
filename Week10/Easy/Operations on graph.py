import sys
class please:
    def __init__(self):
        self.vertices = {}
    def builder(self, edges):
        for i in range(1,edges+1):
            self.vertices[i] = []
    def addEdge(self, n, m):
        self.vertices[n].append(m)
        self.vertices[m].append(n)
    def vertex(self, u):
        if not self.vertices[u]:
            print()
        for p in range(len(self.vertices[u])):
            if p == len(self.vertices[u])-1:
                print(self.vertices[u][p])
            else:
                print(self.vertices[u][p], end = " ")
def main():
    number_of_vertices = int(sys.stdin.readline())
    number_of_operations = int(sys.stdin.readline())
    now = please()
    now.builder(number_of_vertices)
    games = []
    for x in range(number_of_operations):
        d = list(map(int, sys.stdin.readline().split()))
        games.append(d)
    for x in games:
        if x[0] == 1:
            now.addEdge(x[1],x[2])
        else:
            now.vertex(x[1])
main()