'''
1016

어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때,
그 수를 제곱ㄴㄴ수라고 한다.
제곱수는 정수의 제곱이다. min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.
1 4 9 16 25 36 49 64 81 100 . . .

첫째 줄에 두 정수 min과 max가 주어진다.
첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수의 개수를 출력한다.

1 10
7

15 15
1

1 1000
608

1. 소수찾기
 1.1  2 ~ sqrt(max) 까지 에서의 소수 찾기
 1.2
2. 각 소수를 제곱
3. 각 제곱근을 계속 더해주면서 max 보다 클 때 까지 count + 1

소수찾기 : 채 이용
2 ~ sqrt(max) 에서
2로 나누어지는거 지우기
3로 나누어지는거 지우기
 . . .
1000000000000 1000001000000

'''

import math

def primecheck(prime, number): #flag = 0 : 안나눠짐
    flag = 0
    for i in range(0, len(prime)):
        if number % prime[i] == 0:
            flag = prime[i]
            break
    return flag

def jong(prime, min, max):
    array = []
    array.append([0, False])
    for i in range(min, max+1):
        array.append([i, True])
    print(array)

    result= []
    for i in range(0, len(prime)):
        start = min % prime[i]
        start = min + start
        end = max // prime[i]
        resultt = end - start + 2
        result.append(resultt)

    print(result)
    count = 0
    for i in range(0, len(result)):
        count = count + result[i]

    return count
def primeNumber(max):
    n = max
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i*i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes

def start():
    min, max = input().split()
    min = int(min)
    max = int(max)
    sqrtmax = int(math.sqrt(max)) + 1
    prime = primeNumber(sqrtmax)
    result = jong(prime, min, max)

    print(result)

start()