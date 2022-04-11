'''
1014
4
2 3
...
...
2 3
x.x
xxx
2 3
x.x
x.x
10 10
....x.....
..........
..........
..x.......
..........
x...x.x...
.........x
...x......
........x.
.x...x....

4
1
2
46
'''

def jong(array):
    count = []
    for i in range(0, len(array[0])):
        count.append(0)

    for i in range(1, len(array)):
        for j in range(1, len(array[0])):
            if array[i][j] == ".":



def makeArray(n, m):
    array = []
    firstdata = ""
    for i in range(0, m):
        firstdata = firstdata + "x"
    firstdata = firstdata + "x"
    array.append(firstdata)
    for i in range(0, n):
        data = input()
        data = "x" + data
        array.append(data)
    return array

def start():
    testcase = input()
    testcase = int(testcase)
    resultArray = []
    for i in range(0, testcase):
        n, m = input().split()
        n = int(n)
        m = int(m)
        array = makeArray(n, m)
        for i in range(0, len(array)):
            print(array[i])
        result = jong(array)
        resultArray.append(result)

    for i in range(0, testcase):
        print(resultArray[i])
    return
start()











































