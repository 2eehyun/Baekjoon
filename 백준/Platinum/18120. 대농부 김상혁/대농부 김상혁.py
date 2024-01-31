N, A = map(int, input().split())
crops = []
b, c = 0, 0
pos = []

for i in range(N):
    xi, yi, wi = map(int, input().split())
    crops.append([(((xi**2)+(yi**2))**0.5), wi])

crops.sort(key=lambda x: x[0])

# print(crops)
for i in range(N-1):
    dist, w, next = crops[i][0], crops[i][1], crops[i+1][0]
    b, c = b+w, c+w*dist
    axis = b/(2*A)
    if axis<dist:
        pos.append(-A*(dist**2)+b*dist-c)
    elif dist<=axis<next:
        pos.append((b**2)/(4*A)-c)
    


dist, w = crops[N-1][0], crops[N-1][1]
b, c = b+w, c+w*dist
axis = b/(2*A)
pos.append((b**2)/(4*A)-c)

# print(pos)
res = max(pos)
if res<0:
    print(0)
else:
    print(res)
