N = int(input())
first, last = 0, N - 1
idx1, idx2 = 0, N - 1

arr = list(map(int, input().split()))
temp = arr[first] + arr[last]
m = abs(temp)

while first < last:
    temp = arr[first] + arr[last]
    if abs(temp) < m:
        idx1, idx2 = first, last
        m = abs(temp)
    if temp == 0:
        break
    if temp > 0:
        last -= 1
    else:
        first += 1

print(arr[idx1], arr[idx2])