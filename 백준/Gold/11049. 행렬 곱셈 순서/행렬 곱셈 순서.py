N = int(input())
mat = []
dp = [[0]*N for i in range(N)]

for i in range(N):
    mat.append(list(map(int, input().split())))

for d in range(1, N):
    for x in range(N-d):
        y = x+d
        if d==1:
            dp[x][y] = mat[x][0]*mat[x][1]*mat[y][1]
        if d>1:
            cand = []
            for z in range(x, y):
                cand.append(dp[x][z]+dp[z+1][y]+mat[x][0]*mat[z][1]*mat[y][1])
            dp[x][y] = min(cand)
            
print(dp[0][N-1])