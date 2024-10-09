N, M, V = map(int, input().split())
neighborMatrix = [[0] * (N+1) for _ in range(N+1)]
bfsResult, dfsResult = [], []
for _ in range(M):
    a, b = map(int, input().split())
    neighborMatrix[a][b] = 1
    neighborMatrix[b][a] = 1
# print(neighborMatrix)
queue, stack = [V], [V]
# bfs
while queue:
    # print(queue)
    vertex = queue.pop(0)
    if vertex not in bfsResult:
        bfsResult.append(vertex)
    cache = []
    for neighbor in range(1, N+1):
        if neighborMatrix[vertex][neighbor] == 1 and neighbor not in bfsResult:
            cache.append(neighbor)
    # print('bfs: ', cache)
    for item in cache:
        queue.append(item)

# dfs
while stack:
    vertex = stack.pop()
    if vertex not in dfsResult:
        dfsResult.append(vertex)
    cache = []
    for neighbor in range(1, N+1):
        if neighborMatrix[vertex][neighbor] == 1 and neighbor not in dfsResult:
            cache.append(neighbor)
    cache.reverse()
    # print('dfs: ', cache)
    for item in cache:
        stack.append(item)

print(' '.join(map(str, dfsResult)))
print(' '.join(map(str, bfsResult)))