T = int(input())
nums =[] 
for t in range(T):
    nums.append(int(input()))
dp = [[0]*2 for d in range(41)]
dp[0][0], dp[0][1], dp[1][0], dp[1][1] = 1, 0, 0, 1
for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]
for n in nums:
    print(' '.join(map(str, dp[n])))