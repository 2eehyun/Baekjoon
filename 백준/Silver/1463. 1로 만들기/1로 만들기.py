# N, M, V = map(int, input().split())
N = int(input())
dp = [N] * (N+1)
dp[N] = 0
for num in range(N, 1, -1):
    if not (num % 3):
        dp[num // 3] = min(dp[num // 3], dp[num] + 1)
    if not (num % 2):
        dp[num // 2] = min(dp[num // 2], dp[num] + 1)
    dp[num - 1] = min(dp[num - 1], dp[num] + 1)

print(dp[1])