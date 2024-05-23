def merge(left, right):
    idx_l, idx_r= 0, 0
    max_l, max_r = len(left), len(right)
    res = []

    while idx_l<max_l and idx_r<max_r:
        if left[idx_l]<right[idx_r]:
            res.append(left[idx_l])
            idx_l += 1
        else:
            res.append(right[idx_r])
            idx_r += 1
    
    while idx_l<max_l:
        res.append(left[idx_l])
        idx_l += 1
    while idx_r<max_r:
        res.append(right[idx_r])
        idx_r += 1

    return res

def m_sort(arr):
    global limit, value
    if len(arr)==1:
        return arr
    mid = (len(arr)+1)//2
    left = m_sort(arr[:mid])
    right = m_sort(arr[mid:])
    res = merge(left, right)
    # print(res)
    for r in res:
        limit -= 1
        # print(limit, value)
        if not limit:
            value = r
    
    return res

N, K = map(int, input().split())
nums = list(map(int, input().split()))
limit, value = K, -1

m_sort(nums)
print(value)