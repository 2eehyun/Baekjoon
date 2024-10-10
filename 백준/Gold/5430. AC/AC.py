# N, M, V = map(int, input().split())
T = int(input())
res = []
for _ in range(T):
    command_list = list(input())
    count = int(input())
    raw_input = input()
    input_list = []
    if count:
        input_list = raw_input[1:-1].split(',')

    first, last, reverse = 0, count, 0
    reverse = 0
    isValidResult = True
    while command_list:
        command = command_list.pop(0)
        if command=='R':
            reverse += 1
        else:
            if first >= last:
                isValidResult = False
                break
            elif reverse % 2:
                last -= 1
            else:
                first += 1
    
    if isValidResult:
        final_list = input_list[first : last]
        if reverse % 2:
            final_list.reverse()
        res.append('[' + ','.join(final_list) + ']')
    else:
        res.append('error')

for r in res:
    print(r)