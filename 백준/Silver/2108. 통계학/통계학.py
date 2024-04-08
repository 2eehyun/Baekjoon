num=[0]*8001
N = int(input())
for i in range(N):
    num[int(input())+4000]+=1

v1, v2, v3, v4 = 0, 0, 0, 0
sum, mid, first, count, size = 0, 0, 1, 0, 0
M, m, f = 0, 0, 1
fmax = max(num)

for i in range(8001):
    fq = num[i]
    if fq:
        size+=fq
        M=i-4000
        if f:
            f=0
            m=i-4000
        sum+=i*fq
        mid+=fq
        if mid>N//2 and first:
            v2=i-4000
            first=0
        if fmax==fq and count<2:
            v3=i-4000
            count+=1

v1=round((sum/size)-4000)
v4=M-m

print(v1)
print(v2)
print(v3)
print(v4)