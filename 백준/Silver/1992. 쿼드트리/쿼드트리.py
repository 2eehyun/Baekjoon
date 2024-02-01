N = int(input())
board = []
res = ''
for i in range(N):
    board.append(list(input()))
# board = [list('11000011'),list('11000011'),list('00001100'),list('00001100'),list('10001111'),list('01001111'),list('00111111'),list('00111111')]

def check(si, sj, size):
    global res
    color = board[si][sj]
    if size == 1:
        res += color
        return
    same = 1
    for i in range(si, si+size):
        for j in range(sj, sj+size):
            if board[i][j] != color:
                same = 0
    if not same:
        nsize = size//2
        res += '('
        check(si, sj, nsize)
        check(si, sj+nsize, nsize)
        check(si+nsize, sj, nsize)
        check(si+nsize, sj+nsize, nsize)
        res += ')'
    else:
        res += color

check(0, 0, N)
print(res)