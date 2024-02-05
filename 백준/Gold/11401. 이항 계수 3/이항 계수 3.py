def fact(n, p):
    res, i = 1, 1
    while i<n:
        i+=1
        res *= i
        res %= p
    return res

n , k = map(int, input().split())
p = 10**9 + 7
a = fact(n, p)
b = (fact(n-k, p)*fact(k, p))%p
# print(a, b)
num = []

s = p-2
while s>1:
    num.append(s)
    s //= 2
num.reverse()
# print(num)

res = b
for n in num:
    r = res*res
    if n%2:
        r*=b
    res = r%p
    # print(res)

res%=p
print((a*res)%p)