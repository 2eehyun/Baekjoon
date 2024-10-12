N, M = map(int, input().split())
nums = list(map(int, input().split()))
idx_res = []
res = []

def recursive(count, arr = []):
    if count == M:
        idx_res.append(arr)
        return
    
    for idx in range(N):
        if idx in arr:
            continue
        new_arr = arr[:]
        new_arr.append(idx)
        recursive(count+1, new_arr)
    return

nums.sort()
recursive(0)
# print(idx_res)
for arr in idx_res:
    value_arr = []
    for element in arr:
        value_arr.append(nums[element])
    res.append(' '.join(map(str, value_arr)))
# print(res)
for r in res:
    print(r)