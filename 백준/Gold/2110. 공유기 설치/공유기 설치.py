N, C = map(int, input().split())
house = []
for i in range(N):
    house.append(int(input()))
house.sort()
m, M = house[0], house[len(house)-1]
# print(m, M)

def check(d):
    global house, m
    total = 1
    cri = m
    for h in house:
        # print(h, m, 'hs2')
        if h-cri>=d:
            total += 1
            cri = h
            # print('check')
    return total

pos = []
dist = (M-m)//(C-1)
diff = dist
while diff>0:
    diff = diff//2
    res = check(dist)
    # print(dist, res, 'hs1')
    if res>=C:
        pos.append(dist)
        dist = dist+diff
    else:
        dist = dist-diff

if pos:
    s = pos.pop()
    while 1:
        s+=1
        if check(s)<C:
            break
    print(s-1)
else:
    while dist>1:
        dist -= 1
        if check(dist)>=C:
            break
    print(dist)
