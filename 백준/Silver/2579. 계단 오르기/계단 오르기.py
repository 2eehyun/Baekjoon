N = int(input())
scores = []
dp1 = [0] * N
dp2 = [0] * N
for _ in range(N):
    scores.append(int(input()))

dp1[0], dp2[0] = 0, scores[0]
if N > 1:
    dp1[1], dp2[1] = scores[1], scores[0] + scores[1]
    for idx in range(2, N):
        dp1[idx] = max(dp1[idx-2], dp2[idx-2]) + scores[idx]
        dp2[idx] = dp1[idx-1] + scores[idx]

print(max(dp1[N-1], dp2[N-1]))