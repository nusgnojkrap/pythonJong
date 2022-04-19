'''
1199 오일러 회로
어느 점에서 출발하여 그래프 상에 있는 모든 간선을 지나되 한번 지난 간선은 다시 지나지 않고 출발점으로 돌아오는 회로를 오일러 회로라 한다. 단, 그래프는 양방향 그래프가 주어진다.

문제는 그래프가 주어졌을 때 오일러 회로 경로를 출력하는 것이다.

첫 줄에는 정점의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 그리고 다음 N개의 줄에 대해 인접행렬의 정보가 주어진다. i+1번째 줄에는 i번 정점에 대한 인접행렬이 주어진다. 두 정점 사이에 간선이 여러 개 있을 수 있다. 인접행렬의 값은 두 정점 사이의 간선 개수를 의미하며, 0보다 크거나 같고, 10보다 작거나 같은 정수이다.

입력으로 주어지는 그래프에는 루프 (양 끝점이 같은 간선)는 없다. 또, 입력으로 주어지는 그래프는 모두 연결되어 있다.

6
0 1 0 1 1 1
1 0 1 1 1 0
0 1 0 1 0 0
1 1 1 0 1 0
1 1 0 1 0 1
1 0 0 0 1 0

1 2 3 4 1 5 2 4 5 6 1
'''

import sys
import random
sys.setrecursionlimit(10000)


def inputcreate():
    inputN = 1000
    inputArr = []
    for i in range(0, inputN):
        inputArr.append([])
        for j in range(0, inputN):
            inputArr[i].append(0)

    for i in range(0, inputN):
        for j in range(i, inputN):
            if i != j:
                cc = random.randrange(0, 11)
                inputArr[i][j] = cc
                inputArr[j][i] = cc
    return inputArr

def inputtest():
    inputN = 10
    inputArr = []
    for i in range(0, inputN):
        inputArr.append([])
        for j in range(0, inputN):
            inputArr[i].append(0)

    for i in range(0, inputN):
        for j in range(0, inputN):
            if i+1 == j:
                inputArr[i][j] = 1
            elif i == inputN -1:
                if j == inputN -1:
                    inputArr[i][0] =1
    return inputArr

def recursivejong(arr, startpoint, path, ing):
    check = 0
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i][j] != 0:
                check = 1
                break

    if check == 0:
        if startpoint == path[0]:
            path.append(startpoint)
            return [path, 'end']
        else:
            return [-2, 'ing']

    result = [-2, 'ing']
    for i in range(0, len(arr[startpoint])):
        if arr[startpoint][i] != 0:
            copyarr = arr.copy()
            copyarr[startpoint][i] = copyarr[startpoint][i] - 1
            copyarr[i][startpoint] = copyarr[i][startpoint] - 1
            copypath = path.copy()
            copypath.append(i)
            result = recursivejong(copyarr, i, copypath, ing)
            if result[1] == 'end':
                return result

    return result

def jong(arr):
    pointArr = []
    check = 0
    for i in range(0, len(arr)):
        check = check + sum(arr[i])
        pointline = sum(arr[i])
        if pointline % 2 != 0:
            return [-2, 'end']
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
        result = recursivejong(arr, startpointArr[i], pathArr, 'ing')
        if result[0] != -2 :
            if result[0][0] != result[0][-1]:
                result[0].append(result[0][0])
            return result

    return result
def start():
    result = jong(inputtest())
    try:
        result = result[0]
        for i in range(0, len(result)):
            print(str(int(result[i]) + 1), end=" ")
    except:
        result = result + 1
        print(result)

start()
