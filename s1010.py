'''

'''


def start():
    testcase =  input()
    resultArr = []
    maxX = 0
    maxY = 0
    inputArr = []
    for i in range(0, int(testcase)):
        x, y = input().split()
        if maxX < int(x):
            maxX = int(x)
        if maxY < int(y):
            maxY = int(y)
        inputArr.append([x, y])

    globalArr =[]
    globalArr = [([0] * (maxY+1)) for row in range(maxX+1)]
    globalArr[1][1] = 1

    for i in range(1, maxX+1):
        for j in range(i, maxY+1):
            if i == 1:
                globalArr[i][j] = j
            elif i == j:
                globalArr[i][j] = 1
            else:
                globalArr[i][j] = globalArr[i-1][j-1] + globalArr[i][j-1]

    for i in range(0, len(inputArr)):
        xx = inputArr[i][0]
        yy = inputArr[i][1]
        xx = int(xx)
        yy = int(yy)
        print(globalArr[xx][yy])

start()