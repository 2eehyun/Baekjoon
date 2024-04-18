# 1043
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
known, party = [0]*(N+1), []

pp = list(map(int, input().split()))
if (pp.pop(0)):
    for p in pp:
        known[p] = 1

for _ in range(M):
    pp = list(map(int, input().split()))
    party.append(pp[1:])

for _ in range(M):
    for m in range(M):
        check = 0
        for p in party[m]:
            if(known[p]):
                check = 1
                break
        if check:
            for p in party[m]:
                known[p] = 1

res = 0
for m in range(M):
    check = 0
    for p in party[m]:
        if known[p]:
            check = 1
            break
    if not check:
        res += 1
print(res)