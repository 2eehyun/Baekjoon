N = int(input())
nums = list(map(int, input().split()))

arr = [0]*N
for i in range(N):
    arr[i] = 1
    for j in range(i):
        if nums[i]>nums[j]:
            arr[i] = max(arr[i], arr[j]+1)

print(max(arr))