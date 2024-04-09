# 1012
import sys
sys.setrecursionlimit(100000000)

T = int(input())
res = [0]*T
field = []

def findNeighbor(x, y, M, N, t):
    global field
    field[t][y][x] = 0
    if x>0:
        if field[t][y][x-1]:
            findNeighbor(x-1, y, M, N, t)
    if y>0:
        if field[t][y-1][x]:
            findNeighbor(x, y-1, M, N, t)
    if x<M-1:
        if field[t][y][x+1]:
            findNeighbor(x+1, y, M, N, t)
    if y<N-1:
        if field[t][y+1][x]:
            findNeighbor(x, y+1, M, N, t)
    


for t in range(T):
    M, N, K = map(int, input().split())
    field.append([[0]*M for i in range(N)])

    for k in range(K):
        x, y = map(int, input().split())
        field[t][y][x] = 1

    for j in range(N):
        for i in range(M):
            if field[t][j][i]:
                findNeighbor(i, j, M, N, t)
                res[t] += 1

for r in res:
    print(r)