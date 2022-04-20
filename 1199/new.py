'''
1199 오일러 회로

6
0 1 0 1 1 1
1 0 1 1 1 0
0 1 0 1 0 0
1 1 1 0 1 0
1 1 0 1 0 1
1 0 0 0 1 0

1 2 3 4 1 5 2 4 5 6 1
'''
import copy
import sys

sys.setrecursionlimit(10000)
def recursivejong(inputarr, startpoint, path, ing):
    check = 0
    for i in range(0, len(inputarr)):
        for j in range(i, len(inputarr)):
            if inputarr[i][j] != 0:
                check = 1
                break

    if check == 0:
        if startpoint == path[0]:
            return [path, 'end']
        else:
            return [-2, 'ing']

    result = [-2, 'ing']
    for i in range(0, len(inputarr[startpoint])):
        if inputarr[startpoint][i] != 0:
            copyinputarr = inputarr.copy()
            copyinputarr[startpoint][i] = copyinputarr[startpoint][i] - 1
            copyinputarr[i][startpoint] = copyinputarr[i][startpoint] - 1
            copypath = path.copy()
            copypath.append(i)
            result = recursivejong(copyinputarr, i, copypath, ing)
            if result[1] == 'end':
                return result
    return result

def jong(arr):
    pointArr = []
    check = 0
    for i in range(0, len(arr)):
        now = sum(arr[i])
        if now % 2 != 0:
            return -2
        if now == 0:
            return -2
        check = check + sum(arr[i])
        pointline = sum(arr[i])
        pointArr.append(pointline)
    if check ==0:
        return -2
    maxpoint = max(pointArr)
    startpointArr = []
    for i in range(0, len(pointArr)):
        if maxpoint == pointArr[i]:
            startpointArr.append(i)

    for i in range(0, len(startpointArr)):
        pathArr = []
        pathArr.append(startpointArr[i])
        copyarr =copy.deepcopy(arr)
        result = recursivejong(copyarr, startpointArr[i], pathArr, 'ing')
        if result[0] != -2 :
            if result[0][0] != result[0][-1]:
                result[0].append(result[0][0])
            return result

    return result
def start():
    n = input()
    n = int(n)
    inputArr = []
    for i in range(0, n):
        L = list(map(int, input().split()))
        if len(L) == n:
            inputArr.append(L)
        else:
           return
    result = jong(inputArr)
    print("result")
    try:
        result = result[0]
        for i in range(0, len(result)):
            print(str(int(result[i]) + 1), end=" ")
    except:
        result = result + 1
        print(result)

start()