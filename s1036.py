'''
1036 36진수

5
GOOD
LUCK
AND
HAVE
FUN
7

A = 65 - 55 = 10
Z = 90
'''

def deTO36(de):
    firstArr = []
    a = de
    while 1:
        if a < 36:
            firstArr.append(a)
            break
        s, r = divmod(a, 36)
        firstArr.append(r)
        a = s
    resultArr = []
    for i in range(0, len(firstArr)):
        if firstArr[i] < 10:
            resultArr.append(firstArr[i])
        else:
            resultArr.append(chr(firstArr[i]+55))
    resultArr.reverse()
    result = ""
    for i in range(0, len(resultArr)):
        result = result + str(resultArr[i])
    return result


def jong(arr, k):
    result = 0
    weightArr = []
    for i in range(0, 36):
        weightArr.append(0)

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            try:
                now = int(arr[i][j])
                weight = 36**(len(arr[i]) - j - 1)
                sub = (35 - now) * weight
                weightArr[now] = weightArr[now] + sub
                result = result + now * weight
            except:
                now = int(ord(arr[i][j])) - 55
                weight = 36**(len(arr[i]) - j - 1)
                sub = (35 - now) * weight
                weightArr[now] = weightArr[now] + sub
                result = result + now * weight
    weightArr.sort()
    for i in range(0, k):
        result = result + weightArr[35-i]
    return deTO36(result)

def start():
    n = input()
    n = int(n)
    inputArr = []
    for i in range(0, n):
        iput = input()
        inputArr.append(iput)
    k = input()
    k = int(k)
    result = jong(inputArr, k)
    print(result)

start()