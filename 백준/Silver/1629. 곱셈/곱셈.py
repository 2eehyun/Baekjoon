A, B, C = map(int, input().split())
sq = []
temp = B
while temp>1:
    sq.append(temp)
    temp = temp//2
sq.reverse()

num = A%C
for t in sq:
    next = (num*num)%C
    if t%2:
        num = (next*A)%C
    else:
        num = next
    
print(num)