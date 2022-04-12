'''
1027 고층빌딩

15
1 5 3 2 6 3 2 6 4 2 5 7 3 1 5

'''

def jong(arr):
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 1
    countArr = []
    pointArr = []
    for i in range(0, len(arr)):
        pointArr.append([i, arr[i]])
        countArr.append(2)
    countArr[0] = 1
    countArr[-1] = 1

    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            slpy = int(pointArr[j][1] - int(pointArr[i][1]))
            slpx = int(pointArr[j][0] - int(pointArr[i][0]))
            check = 1
            for p in range(i+1, j):
                check = 2
                if pointArr[p][1] * slpx >= slpy * (pointArr[p][0] - int(pointArr[i][0])) + slpx * pointArr[i][1]:
                    check = 0
                    break

            if check == 2:
                countArr[i] = countArr[i] + 1
                countArr[j] = countArr[j] + 1
    print(countArr)
    result = max(countArr)
    return result

def start():
    arraysize = input()
    arraysize = int(arraysize)
    L = list(map(int, input().split()))
    if len(L) != arraysize:
        return
    print(jong(L))
start()









