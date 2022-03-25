'''
1013
(100+1+ | 01)+

3
10010111
011000100110001
0110001011001

NO
NO
YES
'''

def jong(x, result):
    x = list(x)
    print(x)
    if len(x) == 0:
        return result
    if len(x) == 2:
        if x[0] + x[1] =='01':
            return 'YES'
        else:
            return result
    elif len(x) > 2:
        if x[0] + x[1] == '01':
            result = jong(x[2:], 'YES')
        elif x[0] + x[1] + x[2] == '100':
            for i in range(3, len(x)):                  #                        '(100+1+ | 01)+'
                if x[i] == '1':
                    break
            for j in range(i, len(x)-1):
                if x[j] != 1:
                    if x[j+1] == 1:
                        break
            if x[j+1] == 1:
                xx = x[j+1:].copy()
                jong(xx, 'YES')
            else:
                xx = x[j:].copy()
                jong(xx, 'YES')
        else:
            return 'NO'
    else:
        return 'NO'
    return result
def start():
    testcase = input()
    testcase = int(testcase)
    resultArray = []
    for i in range(0, testcase):
        x = input()
        resultArray.append(jong(x, 'NO'))
    for i in range(0, testcase):
        print(resultArray[i])
    return
start()