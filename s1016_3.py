'''
1016

1 10
7
15 15
1
1 1000
608
1000000000000 1000001000000

'''

import math

def jong(prime, min, max):
    array = []
    for i in range(min, max+1):
        array.append(i)

    for i in range(0, len(prime)):
        start = math.ceil(min / prime[i])
        end = max // prime[i]
        for j in range(start, end+1):
            try:
                array[j * prime[i]-min] = 0
            except:
                print("j : " + str(j))
                print("prime[i] : " + str(prime[i]))
                print("j * prime[i] : " + str(j * prime[i]))
    count = 0
    for i in range(0, len(array)):
        if array[i] != 0:
            count = count + 1
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