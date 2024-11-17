N, S = map(int, input().split())
arr = list(map(int, input().split()))
first, last, m = 0, 0, N
if sum(arr) < S:
    print(0)
    N = 0

temp = arr[0]
new = 0
if temp >= S:
    print(1)
    N = 0

for i in range(1, N):
    temp += arr[i]
    if temp >= S:
        if (i + 1) < m:
            m = i + 1
        last = i
        break

while N > 0:
    # print(first, last, temp, m)
    if temp >= S:
        if first == N - 1:
            break
        first += 1
        new = temp - arr[first - 1]
        # print(first, last, new, m)
        if new >= S:
            if (last - first + 1) < m:
                m = last - first + 1
    else:
        if last == N - 1:
            break
        last += 1
        new = temp + arr[last]
        # print(first, last, new, m)
        if new >= S:
            if (last - first + 1) < m:
                m = last - first + 1
    temp = new

if (N != 0):
    print(m)