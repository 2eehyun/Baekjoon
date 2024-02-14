N = int(input())
M = int(input())
res = []
res.append(N*(M%10))
res.append(N*((M%100)//10))
res.append(N*(M//100))
res.append(res[0]+res[1]*10+res[2]*100)
for r in res:
    print(r)