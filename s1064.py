'''
1064

평행사변형은 평행한 두 변을 가진 사각형이다. 세 개의 서로 다른 점이 주어진다. A(xA,yA), B(xB,yB), C(xC,yC)

이때, 적절히 점 D를 찾아서 네 점으로 평행사변형을 만들면 된다. 이때, D가 여러 개 나올 수도 있다.

만들어진 모든 사각형 중 가장 큰 둘레 길이와 가장 작은 둘레 길이의 차이를 출력하는 프로그램을 작성하시오. 만약 만들 수 있는 평행사변형이 없다면 -1을 출력한다.

첫째 줄에 xA yA xB yB xC yC가 주어진다. 모두 절댓값이 5000보다 작거나 같은 정수이다.

첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10-9까지 허용한다
'''
import math

def jong(x1, y1, x2, y2, x3, y3):
    slp12 = "x"
    slp13 = "x"
    slp23 = "x"
    try:
        slp12 = (y2 - y1) / (x2 - x1)
    except:
        slp12 = "x"
    try:
        slp13 = (y3 - y1) / (x3 - x1)
    except:
        slp13 = "x"
    try:
        slp23 = (y3 - y2) / (x3 - x2)
    except:
        slp23 = "x"

    if slp12 == slp13 or slp12 == slp23 or slp23 == slp13:
        return -1.0

    line12 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    line13 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    line23 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)

    lineArray = []
    lineArray.append(line12)
    lineArray.append(line13)
    lineArray.append(line23)
    lineArray.sort()

    result = lineArray[2] - lineArray[0]
    result = result * 2
    return result

def start():
    x1, y1, x2, y2, x3, y3 = input().split()
    result = jong(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3))
    print(result)
    return
start()

