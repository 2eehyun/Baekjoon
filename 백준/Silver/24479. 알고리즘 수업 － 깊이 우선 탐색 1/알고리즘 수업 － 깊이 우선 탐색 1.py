# import sys
# sys.setrecursionlimit(1000000)

N, M, R = map(int, input().split())
neighbor = [[] for _ in range(N+1)]
res = [0]*(N+1)
order = 1

def dfs(n):
    global res, order
    stack = [n]
    while stack:
        node = stack.pop()
        if not res[node]:
            res[node] = order
            order += 1
            for neigh in reversed(neighbor[node]):
                if not res[neigh]:
                    stack.append(neigh)

for _ in range(M):
    u, v = map(int, input().split())
    neighbor[u].append(v)
    neighbor[v].append(u)

for arr in neighbor:
    arr.sort()

dfs(R)
for item in res[1:]:
    print(item)