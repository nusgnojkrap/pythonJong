'''
1012
'''

'''
input
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

output
5
1
'''


def jong(x, y, inputArr):
    newarray = [[0 for col in range(y+1)] for row in range(x+1)]
    count = 0
    for i in range(0, len(inputArr)):
        newarray[int(inputArr[i][0])+1][int(inputArr[i][1]) + 1] = 1

    for i in range(0, len(newarray)):
        print(newarray[i])

    for i in range(0, x+1):
        for j in range(0, y+1):
            if newarray[i][j] ==1:
                if newarray[i-1][j] == 0 and newarray[i][j-1] == 0 :
                    count =count + 1

    return count

def start():
    testcase = input()
    testcase = int(testcase)
    resultArr = []
    for i in range(0, testcase):
        a, b, k = input().split()
        a = int(a)
        b = int(b)
        k = int(k)
        inputArr = []
        for j in range(0, k):
            x, y = input().split()
            x = int(x)
            y = int(y)
            inputArr.append([x, y])

        result = jong(a, b, inputArr)
        resultArr.append(result)
    for i in range(0, testcase):
        print(resultArr[i])
start()

'''
1
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6


'''