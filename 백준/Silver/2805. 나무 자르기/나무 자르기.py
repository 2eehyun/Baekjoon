N, M = map(int, input().split())
tree = list(map(int, input().split()))

def check(h):
    global tree
    total = 0
    for t in tree:
        total += max(t-h, 0)
    return total

pos = [0]
T = max(tree)
len, diff = T, T

while diff>0:
    diff = diff//2
    res = check(len)
    if res>=M:
        pos.append(len)
        len = len+diff
    else:
        len = len-diff

s = pos.pop()
while 1:
    if check(s)<M:
        break
    s+=1
print(s-1)