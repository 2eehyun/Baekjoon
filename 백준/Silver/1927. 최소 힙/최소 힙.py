N = int(input())
Q, res = [], []

def up(id):
    global Q
    target = (id+1)//2-1
    if Q[id]<Q[target]:
        Q[id], Q[target] = Q[target], Q[id]
        return target
    return -1

def down(id):
    global Q
    l, r = (id+1)*2-1, (id+1)*2
    if l>len(Q)-1:
        return -1
    if l==len(Q)-1:
        if Q[l]<Q[id]:
            Q[l], Q[id] = Q[id], Q[l]
            return -1
        return -1
    if Q[l]>Q[r]:
        if Q[r]<Q[id]:
            Q[r], Q[id] = Q[id], Q[r]
            return r
        return -1
    else:
        if Q[l]<Q[id]:
            Q[l], Q[id] = Q[id], Q[l]
            return l
        return -1
    
def delete():
    global Q
    r = Q.pop(0)
    if Q:
        new = Q.pop()
        Q.insert(0, new)
        idx, M = 0, len(Q)//2
        while idx<M:
            target = down(idx)
            if target<0:
                break
            idx = target
    return r

def insert(n):
    global Q
    Q.append(n)
    idx = len(Q)-1
    while idx>0:
        target = up(idx)
        if target<0:
            break
        idx = target

for i in range(N):
    ip = int(input())
    if not ip:
        if Q:
            res.append(delete())
        else:
            res.append(0)
    else:
        insert(ip)

for r in res:
    print(r)