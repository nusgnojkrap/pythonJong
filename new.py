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

def jong(arr, k):
    countArr = []
    weithArr = []
    result = 0
    for i in range(0, 36):
        countArr.append(0)
        weithArr.append([0, i])
    sumArr = []
    for i in range(0, len(arr)):
        sum = 0
        for j in range(len(arr[i]), 0, -1):             # 여기부터 다시 생각
            try:
                now = int(arr[i][j])
                result = result + now
                countArr[now] = countArr[now] + 1
                sum = sum + now
            except:
                now = int(ord(arr[i][j])) - 55
                result = result + now
                countArr[now] = countArr[now] + 1
                sum = sum + now
        sumArr.append(sum)
    print(countArr)
    print("result : " + str(result))
    for i in range(0, 36):
        weith = 35 - i
        weithArr[i][0] = weith * countArr[i]
    print(weithArr)
    weithArr.sort(key=lambda x:x[0])
    print(weithArr[36-k:36])
    sortArr = weithArr[36-k:36]
    for i in range(0, k):
        result = result + sortArr[i][0]
    print("result : " + str(result))

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