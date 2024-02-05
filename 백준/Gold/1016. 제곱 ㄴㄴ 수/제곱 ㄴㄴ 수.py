import math
min, max = map(int, input().split())
num = max-min+1
M = math.floor(max**0.5)

chae = [1]*(M+1)
for i in range(2, M+1):
    if chae[i]:
        mul = i+i
        while mul<=M:
            chae[mul] = 0
            mul += i
psq = []
for i in range(2, M+1):
    if chae[i]:
        psq.append(i*i)

res = [1]*num
for p in psq:
    start = (min//p)
    if min%p:
        start +=1
    start *= p
    while start<=max:
        res[start-min] = 0
        start += p
        
print(res.count(1))