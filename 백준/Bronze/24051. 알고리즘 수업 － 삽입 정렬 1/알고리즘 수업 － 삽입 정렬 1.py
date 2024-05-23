N, K = map(int, input().split())
nums = list(map(int, input().split()))

res, limit= 0, K
for i in range(1, N):
    loc = i-1
    item = nums[i]
    # print(loc)
    if not limit:
        break
    while (loc>=0 and item<nums[loc] and limit):
        nums[loc+1] = nums[loc]
        res = nums[loc]
        loc -= 1
        limit -= 1
        # print(limit, loc, res)
    if loc+1 != i and limit:
        nums[loc+1] = item
        res = item
        limit -= 1
        # print(limit, loc, res)

if limit:
    print(-1)
else:
    print(res)