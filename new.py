'''
1013


3
10010111
011000100110001
0110001011001

NO
NO
YES

(100+1+ | 01)+
'''

def jong(x, result):
    print(x)
    if len(x) == 0:
        return result
    if len(x) == 1:
        result = "NO"
        return result
    elif len(x) == 2:
        if x[0] + x[1] == "01":
            result = "YES"
            result = jong(x[2:], result)
        else:
            result = "NO"
            return result
    else:
        if x[0] + x[1] == "01":
            result = "YES"
            result = jong(x[2:], result)
        elif x[0] + x[1] + x[2] == "100":
            result = "YES"
            for i in range(3, len(x)):
                if x[i] == "1":
                    break
            flag = 0
            for j in range(i, len(x)):
                if x[j] == "0":
                    flag=1
                    break
            if flag == 1:

            if x[j] == '1':
                if [j+1] == '1':
                result= jong(x[j+1:], result)
            else:
                result = jong(x[j:], result)
        else:
            result = "NO"
            return result


    return result


def start():
    testcase = input()
    testcase = int(testcase)
    resultArray = []
    for i in range(0, testcase):
        x = input()
        x = list(x)
        resultArray.append(jong(x, "NO"))
    for i in range(0, testcase):
        print(resultArray[i])
    return
start()