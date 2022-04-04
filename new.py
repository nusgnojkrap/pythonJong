'''
1017
지민이는 수의 리스트가 있을 때, 이를 짝지어 각 쌍의 합이 소수가 되게 하려고 한다. 예를 들어, {1, 4, 7, 10, 11, 12}가 있다고 하자. 지민이는 다음과 같이 짝지을 수 있다.

1 + 4 = 5, 7 + 10 = 17, 11 + 12 = 23

또는

1 + 10 = 11, 4 + 7 = 11, 11 + 12 = 23

수의 리스트가 주어졌을 때, 지민이가 모든 수를 다 짝지었을 때, 첫 번째 수와 어떤 수를 짝지었는지 오름차순으로 출력하는 프로그램을 작성하시오. 위의 예제에서 1 + 12 = 13으로 소수이다. 그러나, 남은 4개의 수를 합이 소수가 되게 짝지을 수 있는 방법이 없다. 따라서 위의 경우 정답은 4, 10이다.


첫째 줄에 리스트의 크기 N이 주어진다. N은 50보다 작거나 같은 자연수이며, 짝수이다. 둘째 줄에 리스트에 들어있는 수가 주어진다. 리스트에 들어있는 수는 1,000보다 작거나 같은 자연수이며, 중복되지 않는다.

첫째 줄에 정답을 출력한다. 없으면 -1을 출력한다.
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
            array[j * prime[i] - min] = 0

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