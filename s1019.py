'''
1019 책 페이지
'''

def jong(n):
    arr = []
    for i in range(0, 10):
        arr.append(0)




    for i in range(1, n+1):
        number = i
        number = str(number)
        for j in range(0, len(number)):
            arr[int(number[j])] = arr[int(number[j])] + 1


    return arr

def start():
    n = input()
    n = int(n)
    arr = jong(n)
    for i in range(0, len(arr)):
        print(arr[i], end=" ")
    return
start()