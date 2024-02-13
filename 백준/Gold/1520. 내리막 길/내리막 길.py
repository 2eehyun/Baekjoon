M, N = map(int, input().split())
arr = []
for i in range(M):
    arr.append(list(map(int, input().split())))

dp = [[-1]*N for i in range(M)]

def check(x, y):
    res = [1, 1, 1, 1]
    if not x:
        res[0] = 0
    if not y:
        res[1] = 0
    if x==M-1:
        res[2] = 0
    if y==N-1:
        res[3] = 0
    return res

def go(x, y):
    r1, r2, r3, r4 = 0,0,0,0
    if dp[x][y]>=0:
        return dp[x][y]
    if x==M-1 and y==N-1:
        return 1
    pos = check(x, y)
    if pos[0]:
        if arr[x][y]>arr[x-1][y]:
            r1 = go(x-1, y)
            # print(x, y, 'hs1', r1)
            dp[x-1][y] = r1
    if pos[1]:
        if arr[x][y]>arr[x][y-1]:
            r2 = go(x, y-1)
            # print(x, y, 'hs2', r2)
            dp[x][y-1] = r2
    if pos[2]:
        if arr[x][y]>arr[x+1][y]:
            r3 = go(x+1, y)
            # print(x, y, 'hs3', r3)
            dp[x+1][y] = r3
    if pos[3]:
        if arr[x][y]>arr[x][y+1]:
            r4 = go(x, y+1)
            # print(x, y, 'hs4', r4)
            dp[x][y+1] = r4
    r = r1+r2+r3+r4
    dp[x][y] = r
    # print(dp, x, y, r)
    return r

print(go(0, 0))