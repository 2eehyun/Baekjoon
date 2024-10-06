N = int(input())
prevMIN = [0, 0, 0]
prevMAX = [0, 0, 0]
tempMIN = [0, 0, 0]
tempMAX = [0, 0, 0]

elem0, elem1, elem2 = map(int, input().split())
prevMIN[0], prevMIN[1], prevMIN[2] = elem0, elem1, elem2
prevMAX[0], prevMAX[1], prevMAX[2] = elem0, elem1, elem2
tempMIN[0], tempMIN[1], tempMIN[2] = elem0, elem1, elem2
tempMAX[0], tempMAX[1], tempMAX[2] = elem0, elem1, elem2

for i in range(1, N):
    elem0, elem1, elem2 = map(int, input().split())
    tempMIN[0] = min(prevMIN[0], prevMIN[1]) + elem0
    tempMIN[1] = min(prevMIN[0], prevMIN[1], prevMIN[2]) + elem1
    tempMIN[2] = min(prevMIN[1], prevMIN[2]) + elem2

    tempMAX[0] = max(prevMAX[0], prevMAX[1]) + elem0
    tempMAX[1] = max(prevMAX[0], prevMAX[1], prevMAX[2]) + elem1
    tempMAX[2] = max(prevMAX[1], prevMAX[2]) + elem2

    prevMIN[0], prevMIN[1], prevMIN[2] = tempMIN[0], tempMIN[1], tempMIN[2]
    prevMAX[0], prevMAX[1], prevMAX[2] = tempMAX[0], tempMAX[1], tempMAX[2]

print(max(tempMAX[0], tempMAX[1], tempMAX[2]), min(tempMIN[0], tempMIN[1], tempMIN[2]))