def jun(a, b, count):
    a = int(a)
    b = int(b)
    if a == 0:
        return b
    if a == b:
        return 1
    for i in range(0, b-a):
        count = count + jun(a-1, b-i-1, count)
    return count


def start():
    testcase =  input()
    resultArr = []
    for i in range(0, int(testcase)):
        x, y = input().split()
        x = int(x)
        y = int(y)
        X = [0 for i in range(x)]
        Y = [0 for i in range(y)]
        result = jun(x, y, 0)
        resultArr.append(result)
    for i in range(0, int(testcase)):
        print(str(resultArr[i]))
start()