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


def primecheck(prime, number):
    flag = 0
    for i in range(0, len(prime)):
        if number % prime[i] == 0:
            flag = prime[i]
            break
    return flag

def jong(prime, min, max):
    prime2 = []
    leen = max - min
    for i in range(0, len(prime)):
        prime2.append(int(prime[i]) * int(prime[i]))
    array = []
    for i in range(min, max + 1):
        array.append(i)
    for i in range(0, len(array)):
        if array[i] != 0:
            checkprime = primecheck(prime2, array[i])
            if checkprime != 0: #해당 경우의 배수를 array에서 모두 삭제 첫 번째부터 전부 삭제
                last = leen // checkprime
                for j in range(0, last):
                    if len(array) < i + j*checkprime:
                        break
                    array[i + j*checkprime] = 0

    count = 0
    for i in range(0, len(array)):
        if array[i] !=0:
            count = count + 1
    return count

def primeNumber(max):
    number = []
    for i in range(0, max - 1):
        number.append(i + 2)
    for i in range(0, max - 1):
        if number[i] != 0:
            for j in range(i + 1, max):
                if j == len(number):
                    break
                else:
                    if number[j] != 0:
                        if number[j] % number[i] == 0:
                            number[j] = 0
    prime = []
    for i in range(0, len(number)):
        if number[i] != 0:
            prime.append(number[i])
    return prime


def start():
    min, max = input().split()
    min = int(min)
    max = int(max)
    sqrtmax = int(math.sqrt(max)) + 1
    prime = primeNumber(sqrtmax)
    print(prime)
    return
    result = jong(prime, min, max)

    print(result)


start()
