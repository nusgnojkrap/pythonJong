'''
1019 책 페이지
'''

def jong(n):
    arr = []
    for i in range(0, 10):
        arr.append(0)
    strn = str(n)
    for i in range(len(strn), 0, -1):
        print("strn[i-1] : " + strn[i-1])
        intn = strn[i-1]


    return arr
def start():
    n = input()
    n = int(n)
    arr = jong(n)
    for i in range(0, len(arr)):
        print(arr[i], end = " ")
    return
start()