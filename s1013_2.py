'''
1013


3
10010111
011000100110001
0110001011001

NO
NO
YES

2개 이상
4개 이상

(100+1+ | 01)+
'''

def jong(x, result):
    print(x)
    if result == "NO":
        return result
    try:
        if x[0] + x[1] + x[2] == "100":
            if x[4] != "1":
                result = "NO"
                return result
            else:
                for i in range(0, len(x)):
                    if x[i] == "1":
                        break
                    i = i - 1
                    result = "YES"
                    result = jong(x[i:], result)
                    return result
    except:
        try:
            if x[0] + x[1] == "01":
                result = "YES"
                result = jong(x[2:], result)
                return result
            else:
                result = "NO"
                return result
        except:
            result = "NO"
            return result






def start():
    testcase = input()
    testcase = int(testcase)
    resultArray = []
    for i in range(0, testcase):
        x = input()
        x = list(x)
        resultArray.append(jong(x, "start"))
    for i in range(0, testcase):
        print(resultArray[i])
    return
start()