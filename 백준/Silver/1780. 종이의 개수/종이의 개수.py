N = int(input())
board = []
res = [0, 0, 0]
for i in range(N):
    board.append(list(map(int, input().split())))
# board = [list('11000011'),list('11000011'),list('00001100'),list('00001100'),list('10001111'),list('01001111'),list('00111111'),list('00111111')]

def check(si, sj, size):
    color = board[si][sj]
    if size == 1:
        res[color+1] += 1
        return
    same = 1
    for i in range(si, si+size):
        for j in range(sj, sj+size):
            if board[i][j] != color:
                same = 0
    if not same:
        nsize = size//3
        check(si, sj, nsize)
        check(si, sj+nsize, nsize)
        check(si, sj+2*nsize, nsize)
        check(si+nsize, sj, nsize)
        check(si+nsize, sj+nsize, nsize)
        check(si+nsize, sj+2*nsize, nsize)
        check(si+2*nsize, sj, nsize)
        check(si+2*nsize, sj+nsize, nsize)
        check(si+2*nsize, sj+2*nsize, nsize)
    else:
        res[color+1] += 1

check(0, 0, N)
print(res[0])
print(res[1])
print(res[2])