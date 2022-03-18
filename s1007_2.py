'''
1007
'''
import math
miniii = []
def jongsun(case, a, b, sumx, sumy, n, minire):
    print("----")
    print(sumx)
    print(minire)
    print(case)
    if len(case)* 2 == int(n):
        result = (a - 2 * sumx)*(a - 2 * sumx) + (b - 2 * sumy)*(b - 2 * sumy)
        try:
            if minire == -1:
                minire = result
            elif minire > result:
                minire = result
            return minire
        except:
            print("if")
            print(case)
            print("minire : " + str(minire))
            print("result : " + str(result))
            print("-----")
            exit(0)


    for i in range (0, len(case)):
        sumx = sumx + int(case[i][0])
        sumy = sumy + int(case[i][1])
        ppp = case[i]
        popArr = case.copy()
        popArr.pop(i)
        newmini = int(jongsun(popArr, a, b, sumx, sumy, n, min))
        try:
            if minire == -1:
                minire = newmini
            elif minire > newmini:
                minire = newmini
        except:
            print("minire : " + str(minire))
            print("newmini : " + str(newmini))
        sumx = sumx - int(case[i][0])
        sumy = sumy - int(case[i][1])

def ahrl(case):
    allx = 0
    ally = 0

    for i in range(0, len(case)):
        allx = allx + int(case[i][0])
        ally = ally + int(case[i][1])

    result = jongsun(case, allx, ally, 0, 0, len(case), -1)

    #result = min(miniii, key=lambda x: float(x))
    print(result)
    result = math.sqrt(result)
    print(result)
    return result
##|sum| = 2 * sqrt( v(xn - allx/2)^2 + (yn - ally/2)^2 )
def startinput():
    result = []
    testcase = input()
    for i in range(0, int(testcase)):
        n = input()
        case = []
        for i in range(0, int(n)):
            x, y = input().split()
            case.append([x, y])
        result.append(ahrl(case))

    #for i in range(0, len(result)):
        #print(result[i])
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