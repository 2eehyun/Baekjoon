arr = []
N = int(input())
for _ in range(N):
    arr.append(list(map(int, input().split())))

result = 0
for i in range(N - 1):
    result = result + arr[i][0] * arr[i + 1][1] - arr[i][1] * arr[i + 1][0]
result = result + arr[N - 1][0] * arr[0][1] - arr[N - 1][1] * arr[0][0]
print(round(abs(result / 2), 1))