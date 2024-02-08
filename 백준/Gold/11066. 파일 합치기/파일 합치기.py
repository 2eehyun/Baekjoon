T = int(input())
res = []
for i in range(T):
    K = int(input())
    file = list(map(int, input().split()))

    sum, t = [], 0
    for f in file:
        t += f
        sum.append(t)

    dp = [[0]*K for k in range(K)]
    for d in range(K):
        for x in range(K-d):
            y = x+d
            if not d:
                dp[x][y] = file[x]
            elif d==1:
                dp[x][y] = file[x]+file[y]
            else:
                cand = []
                part = sum[y]
                if x:
                    part -= sum[x-1]
                cand.append(dp[x+1][y]+part)
                for z in range(x+1, y-1):
                    cand.append(dp[x][z]+dp[z+1][y]+part)
                cand.append(dp[x][y-1]+part)
                # print(cand)
                dp[x][y] = min(cand)
    res.append(dp[0][K-1])

for r in res:
    print(r)