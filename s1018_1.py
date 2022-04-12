'''
1018 체스판
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
'''

def jong(arr, m, n):
   min = 2500
   for p in range(0, m-7):
       for q in range(0, n-7):
           count1 = 0
           count2 = 0
           for i in range(p, p+8):
               for j in range(q, q+8):
                   if i % 2 == 0:
                       if j % 2 == 0:
                           if arr[i][j] == "W":
                               count2 = count2 + 1
                           else:
                               count1 = count1 + 1
                       else:
                           if arr[i][j] == "B":
                               count2 = count2 + 1
                           else:
                               count1 = count1 + 1
                   else:
                       if j % 2 == 0:
                           if arr[i][j] == "B":
                               count2 = count2 + 1
                           else:
                               count1 = count1 + 1
                       else:
                           if arr[i][j] == "W":
                               count2 = count2 + 1
                           else:
                               count1 = count1 + 1
           if count1 > count2:
               if min > count2 :
                   min = count2
           else:
               if min > count1 :
                   min = count1
   return min

def start():
    m, n = map(int, input().split())
    inputArr = []
    for i in range(0, m):
        L = input()
        if len(L) != n:
            return
        inputArr.append(L)
    print(jong(inputArr, m, n))
start()


