globalpath = []
def calculate(path, timedb, goal):
    new = 0
    s = 0
    if len(path) == 0:
        return timedb[int(goal) -1]
    for i in range(0, len(path)):
        new = new + int(timedb[int(path[i]) - 1])
        if i+1 == len(path) or path[i+1] == goal:
            if s <= new:
                s = new
            new = 0
    return s

def recursivefun(ruleDB, goal, path, testcase):
    count = 0
    p = []
    for i in range(0, len(ruleDB)):
        if goal == ruleDB[i][0][1]:
            count = count + 1
            path.append(ruleDB[i][0][0])
            pop_rule = ruleDB[i]
            ggg = ruleDB[i][0][0]
            ruleDB.pop(i)
            p.append(path)
            k = recursivefun(ruleDB, ggg, path, testcase)
            ruleDB.insert(i, pop_rule)
            if k != None:
                globalpath[testcase].extend(k)
            path.pop()
    if count == 0:
        return path

def starcraft(timedb, ruleDB, goal, testcase):
    path = []
    path.append(goal)
    recursivefun(ruleDB, goal, path, testcase)
    return calculate(globalpath[testcase], timedb, goal)

def startf():
    testcase = input()
    result = []
    for i in range(0, int(testcase)):
        globalpath.append([])
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