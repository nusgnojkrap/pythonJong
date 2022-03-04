#문제 1005

# 프로게이머 최백준은 애인과의 데이트 비용을 마련하기 위해 서강대학교배 ACM크래프트 대회에 참가했다!
# 최백준은 화려한 컨트롤 실력을 가지고 있기 때문에 모든 경기에서 특정 건물만 짓는다면 무조건 게임에서 이길 수 있다.
# 그러나 매 게임마다 특정건물을 짓기 위한 순서가 달라지므로 최백준은 좌절하고 있었다.
# 백준이를 위해 특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내는 프로그램을 작성해주자.

#첫째 줄에는 테스트케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 다음과 같이 주어진다.
# 첫째 줄에 건물의 개수 N과 건물간의 건설순서 규칙의 총 개수 K이 주어진다. (건물의 번호는 1번부터 N번까지 존재한다)

#둘째 줄에는 각 건물당 건설에 걸리는 시간 D1, D2, ..., DN이 공백을 사이로 주어진다.
# 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. (이는 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미이다)

#마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.

#건물 W를 건설완료 하는데 드는 최소 시간을 출력한다.
# 편의상 건물을 짓는 명령을 내리는 데는 시간이 소요되지 않는다고 가정한다.

#건설순서는 모든 건물이 건설 가능하도록 주어진다.

#2 ≤ N ≤ 1000
#1 ≤ K ≤ 100,000
#1 ≤ X, Y, W ≤ N
#0 ≤ Di ≤ 100,000, Di는 정수


###################################################################
def timecalculate(path, time):
    max = 0
    for i in range(0, len(path)):
        max = max + int(time[int(path[i]) - 1])
    return max

def recursivefun(ruleDB, goal, path, timedb):
    check = 0
    maxtime = 0
    for i in range(0, len(ruleDB)):
        if ruleDB[i][0][1] == goal:
            check = 1
            path.append(ruleDB[i][0][0])
            save_goal = ruleDB[i][0][0]
            pop_rule = ruleDB[i]
            ruleDB.pop(i)
            t = recursivefun(ruleDB, save_goal, path, timedb)
            ruleDB.insert(i, pop_rule)
            path.pop()
            if maxtime < t or maxtime == t:
                maxtime = t

    if check == 0:
        maxtime = timecalculate(path, timedb)
    return maxtime
############################################################################

def starcraft(timedb, ruleDB, goal, testcase):
    for i in range(0, len(ruleDB)):
        if ruleDB[i][0] == goal:
            ruleDB.pop(i)
    path = []
    path.append(goal)
    a = recursivefun(ruleDB, goal, path, timedb)
    return a

def startf():
    testcase = input()
    result = []
    for i in range(0, int(testcase)):
        count, rule = input().split()
        time = []
        time = input().split()
        ruleDB = []
        for j in range(0, int(rule)):
            ruleDB.append([])
            a, b = input().split()
            ruleDB[j] = []
            ruleDB[j].append([a, b])

        goal = input()
        r = starcraft(time, ruleDB, goal, i)
        result.append(r)

    for i in range(0, len(result)):
        print(result[i])
startf()
