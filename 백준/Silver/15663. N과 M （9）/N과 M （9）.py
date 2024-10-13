N, M = map(int, input().split())
nums = list(map(int, input().split()))
value_res = []
res = []
checked = [False] * N

nums.sort()

def recursive(count, arr = []):
    if count == M:
        value_res.append(arr)
        return
    
    last = 0
    for idx in range(N):
        if checked[idx] or nums[idx] == last:
            continue
        last = nums[idx]
        new_arr = arr[:]
        new_arr.append(nums[idx])
        checked[idx] = True
        recursive(count+1, new_arr)
        checked[idx] = False
    return

recursive(0)

for arr in value_res:
    res.append(' '.join(map(str, arr)))

for r in res:
    print(r)