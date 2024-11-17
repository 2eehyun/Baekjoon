edgeArr = []
id = 0
result = 0
V, E = map(int, input().split())
choosed = [-1] * (V + 1)
for i in range(E):
    edgeArr.append(list(map(int, input().split())))
edgeArr.sort(key = lambda edge: edge[2])

for edge in edgeArr:
    if choosed[edge[0]] == choosed[edge[1]] != -1:
        continue

    result += edge[2]
    if choosed[edge[0]] == choosed[edge[1]]:
        choosed[edge[0]] = id
        choosed[edge[1]] = id
        id += 1
    elif choosed[edge[0]] == -1:
        choosed[edge[0]] = choosed[edge[1]]
    elif choosed[edge[1]] == -1:
        choosed[edge[1]] = choosed[edge[0]]
    else:
        m = min(choosed[edge[0]], choosed[edge[1]])
        M = max(choosed[edge[0]], choosed[edge[1]])
        for v in range(V + 1):
            if choosed[v] == M:
                choosed[v] = m

print(result)