N = int(input())
nums = list(map(int, input().split()))

dp = [0]*N
for i in range(N):
    dp[i] = nums[i]
    for j in range(i):
        if nums[j]<nums[i]:
            dp[i] = max(dp[i], dp[j]+nums[i])

print(max(dp))