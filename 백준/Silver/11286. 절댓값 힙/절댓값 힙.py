N = int(input())
pQ, nQ, res = [], [], []

def pup(id):
    global pQ
    target = (id+1)//2-1
    if pQ[id]<pQ[target]:
        pQ[id], pQ[target] = pQ[target], pQ[id]
        return target
    return -1

def nup(id):
    global nQ
    target = (id+1)//2-1
    if nQ[id]>nQ[target]:
        nQ[id], nQ[target] = nQ[target], nQ[id]
        return target
    return -1

def pdown(id):
    global pQ
    l, r = (id+1)*2-1, (id+1)*2
    if l>len(pQ)-1:
        return -1
    if l==len(pQ)-1:
        if pQ[l]<pQ[id]:
            pQ[l], pQ[id] = pQ[id], pQ[l]
            return -1
        return -1
    if pQ[l]>pQ[r]:
        if pQ[r]<pQ[id]:
            pQ[r], pQ[id] = pQ[id], pQ[r]
            return r
        return -1
    else:
        if pQ[l]<pQ[id]:
            pQ[l], pQ[id] = pQ[id], pQ[l]
            return l
        return -1

def ndown(id):
    global nQ
    l, r = (id+1)*2-1, (id+1)*2
    if l>len(nQ)-1:
        return -1
    if l==len(nQ)-1:
        if nQ[l]>nQ[id]:
            nQ[l], nQ[id] = nQ[id], nQ[l]
            return -1
        return -1
    if nQ[l]<nQ[r]:
        if nQ[r]>nQ[id]:
            nQ[r], nQ[id] = nQ[id], nQ[r]
            return r
        return -1
    else:
        if nQ[l]>nQ[id]:
            nQ[l], nQ[id] = nQ[id], nQ[l]
            return l
        return -1
    
def delete(pos):
    global pQ, nQ
    if pos>0:
        r = pQ.pop(0)
        if pQ:
            new = pQ.pop()
            pQ.insert(0, new)
            idx, M = 0, len(pQ)//2
            while idx<M:
                target = pdown(idx)
                if target<0:
                    break
                idx = target
        return r
    else:
        r = nQ.pop(0)
        if nQ:
            new = nQ.pop()
            nQ.insert(0, new)
            idx, M = 0, len(nQ)//2
            while idx<M:
                target = ndown(idx)
                if target<0:
                    break
                idx = target
        return r
        

def insert(n):
    global pQ, nQ
    if n>0:
        pQ.append(n)
        idx = len(pQ)-1
        while idx>0:
            target = pup(idx)
            if target<0:
                break
            idx = target
    else:
        nQ.append(n)
        idx = len(nQ)-1
        while idx>0:
            target = nup(idx)
            if target<0:
                break
            idx = target

for i in range(N):
    ip = int(input())
    if not ip:
        if not pQ and not nQ:
            res.append(0)
        elif not pQ:
            res.append(delete(0))
        elif not nQ:
            res.append(delete(1))
        else:
            if pQ[0]<abs(nQ[0]):
                res.append(delete(1))
            else:
                res.append(delete(0))
                
    else:
        insert(ip)

for r in res:
    print(r)