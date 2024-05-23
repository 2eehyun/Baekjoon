N, K = map(int, input().split())
nums = list(map(int, input().split()))

res, limit, fin = [], K, False
for idx in range(N+1):
    # print(limit, nums)
    if not nums:
        fin = True
        break
    if not limit:
        break
    last = N-1-idx
    M = max(nums)
    # print(nums)
    t_idx = nums.index(M)
    if t_idx != last:
        res = [nums[last], nums[t_idx]]
        nums[t_idx], nums[last] = nums[last], nums[t_idx]
        limit -= 1
        # print(nums[last])
    nums.pop()

if fin:
    print(-1)
else:
    for r in res:
        print(r, end = ' ')