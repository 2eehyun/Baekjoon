A, B= [], []
N, M = map(int, input().split())
for i in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
for i in range(M):
    B.append(list(map(int, input().split())))

res = [[0]*K for i in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            res[i][j] += A[i][k]*B[k][j]
        
rr = []
for i in res:
    for j in i:
        print(j, end = ' ')
    print()