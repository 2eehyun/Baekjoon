N = int(input())
matrix, num = [[1, 1], [1, 0]], []

i = N
while i>1:
    num.append(i)
    i //= 2
num.reverse()

def mul(m1, m2):
    res = [[0]*2 for n in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += m1[i][k]*m2[k][j]
            res[i][j] %= ((10**9)+7)
    return res

m = matrix
for n in num:
    nm = mul(m, m)
    if n%2:
        nm = mul(nm, matrix)
    m = nm

print(m[1][0]%((10**9)+7))
