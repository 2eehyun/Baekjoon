N, R, C = map(int, input().split())
res, factor = 0, 2**(N-1)
for i in range(N): # 0~N-1
    res += ((R//factor)*2+(C//factor))*factor*factor
    # print('i:', i, 'factor:', factor, 'temp:', res)
    R %= factor
    C %= factor
    factor //= 2

print(res)