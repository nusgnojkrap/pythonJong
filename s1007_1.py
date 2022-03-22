'''
1007
'''
import math
def jong(case, a, b, sumX, sumY, n, min, position):
    if int(position) == 0:
        result = (a - 2 * sumX) * (a - 2 * sumX) + (b - 2 * sumY) * (b - 2 * sumY)
        if min == -1:
            min = result
            return min
        if min > result:
            min = result
        return min

    for i in range(0, len(case) - int(position)):
        sumX = sumX + int(case[i][0])
        sumY = sumY + int(case[i][1])
        copyArr = case[i+1:].copy()
        min = jong(copyArr, a, b, sumX, sumY, n, min, int(position)-1)
        sumX = sumX - int(case[i][0])
        sumY = sumY - int(case[i][1])

    return min

def ahrl(case):
    allx = 0
    ally = 0

    for i in range(0, len(case)):
        allx = allx + int(case[i][0])
        ally = ally + int(case[i][1])

    n = len(case)
    n = int(n)
    position = n / 2
    position = int(position)
    result = jong(case, allx, ally, 0, 0, n, -1, position)
    result = math.sqrt(result)
    return result

##|sum| = 2 * sqrt( v(xn - allx/2)^2 + (yn - ally/2)^2 )
def startinput():
    result = []
    testcase = input()
    testcase = int(testcase)
    for i in range(0, testcase):
        n = input()
        n = int(n)
        case = []
        for j in range(0, n):
            x, y = input().split()
            case.append([x, y])
        result.append(ahrl(case))

    for i in range(0, len(result)):
        print(result[i])

startinput()


'''
2
4
5 5
5 -5
-5 5
-5 -5
2
-100000 -100000
100000 100000

1
10
26 -76
65 -83
78 38
92 22
-60 -42
-27 85
42 46
-86 98
92 -47
-41 38

0.000000000000
282842.712474619038

13.341664064126334

'''